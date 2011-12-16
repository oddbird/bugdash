from collections import defaultdict
import datetime
import re

from django.conf import settings
from django.utils.dateformat import format

from bugzilla.models import Bug
from dateutil.parser import parse

from .areas import AREAS



WHITEBOARD_RE = re.compile(settings.BUGDASH_WHITEBOARD_RE)


SEVERITIES = [
    "enhancement",
    "trivial",
    "minor",
    "normal",
    "major",
    "critical",
    "blocker",
    ]


class DashBug(Bug):
    """
    A Bugzilla ``Bug`` for display in the dashboard.

    """
    def __init__(self, *args, **kwargs):
        super(DashBug, self).__init__(*args, **kwargs)
        self._deadline = None
        self._area = None


    def _parse_deadline_and_area(self):
        match = WHITEBOARD_RE.search(self.whiteboard)
        if match:
            data = match.groupdict()
            self._deadline = parse(data["deadline"]).date()
            self._area = AREAS.by_name(data["area"])
        else:
            self._deadline = datetime.date.today()
            self._area = AREAS.unknown


    @property
    def deadline(self):
        if self._deadline is None:
            self._parse_deadline_and_area()
        return self._deadline


    @property
    def area(self):
        if self._area is None:
            self._parse_deadline_and_area()
        return self._area


    @property
    def web_url(self):
        return settings.BUGZILLA_BUG_URL_BASE + str(self.id)


    @property
    def severity_numeric(self):
        """
        A numeric representation of the severity, which allows ordering by it.

        """
        try:
            return SEVERITIES.index(self.severity)
        except ValueError:
            # unknown severity is least severe
            return len(SEVERITIES)



class Dashboard(object):
    """
    A list of bugs bucketed by deadline into intervals of given length in days.

    Bugs must have a "deadline" attribute which is a ``datetime.date``, and an
    ``area`` attribute which is an ``Area``.

    Initial interval ("overdue") has no start date and end date of yesterday.

    """
    def __init__(self, bugs, interval_length):
        """
        Create a ``Dashboard`` with given bugs list and period length in days.

        """
        delta = datetime.timedelta(days=interval_length-1)
        one_day = datetime.timedelta(days=1)
        today = datetime.date.today()
        # list of intervals, starting from today, with no gaps
        # first interval may be "overdue", only if there are overdue bugs
        self.intervals = []
        for bug in sorted(bugs, key=lambda b: b.deadline):
            if not self.intervals:
                if bug.deadline < today:
                    self.intervals.append(Interval(None, today - one_day))
                else:
                    self.intervals.append(Interval(today, today + delta))
            while bug.deadline > self.intervals[-1].end:
                start = self.intervals[-1].end + one_day
                self.intervals.append(Interval(start, start + delta))
            self.intervals[-1].add(bug)


    def __iter__(self):
        """
        Yields intervals when iterated.

        """
        return iter(self.intervals)



def format_date_range(start, end, today=None):
    if today is None:
        today = datetime.date.today()

    if start.year == end.year:
        if start == end:
            ret = format(start, "b j")
        elif start.month == end.month:
            ret = "%s %s - %s" % (
                format(start, "b"), start.day, end.day)
        else:
            ret = "%s - %s" % (
                format(start, "b j"), format(end, "b j"))
        if start.year != today.year:
            ret = "%s %s" % (ret, start.year)
    else:
        ret = "%s - %s" % (
            format(start, "b j"), format(end, "b j"))

    return ret



class BugCollection(object):
    """
    A collection of bugs that tracks counts by area.

    """
    def __init__(self):
        # maps area id to count of bugs
        self._area_counts = defaultdict(lambda: 0)
        self._bugs = []


    @property
    def bugs(self):
        """
        List of bugs in this collection, sorted from most to least severe.

        """
        return sorted(
            self._bugs, key=lambda b: b.severity_numeric, reverse=True)


    @property
    def summary(self):
        """
        Iterable of areas in this collection, each annotated with bugcount.

        """
        for area in AREAS:
            area.bugcount = self._area_counts[area.id]
            if area.bugcount:
                yield area


    def add(self, bug):
        """
        Add given bug to this collection.

        """
        self._bugs.append(bug)
        self._area_counts[bug.area.id] += 1



class Day(BugCollection):
    """
    A list of bugs due on a given day, sorted by severity.

    """
    def __init__(self, date):
        """
        Create a ``Day`` for the given date.

        """
        super(Day, self).__init__()
        self.date = date


    def add(self, bug):
        """
        Add given bug to this day.

        Raises ``ValueError`` if the bug's deadline is not on this day.

        """
        if bug.deadline != self.date:
            raise ValueError(
                "Bug deadline %s is not on date %s"
                % (bug.deadline, self.date))
        return super(Day, self).add(bug)



class Interval(BugCollection):
    """
    A list of bugs in a given time interval, bucketed by deadline day.

    """
    def __init__(self, start, end):
        """
        Create an ``Interval`` with given start and end day.

        """
        super(Interval, self).__init__()
        self.start = start
        self.end = end
        # maps individual date to Day
        self._by_deadline = defaultdict(list)


    @property
    def title(self, today=None):
        """
        Either "overdue" or a concise description of the date range.

        """
        if self.start is None:
            return "overdue"

        return format_date_range(self.start, self.end, today)


    @property
    def days(self):
        """
        List of Days in deadline order.

        """
        return sorted(
            [day for day in self._by_deadline.values()],
            key=lambda i: i.date
            )


    @property
    def overdue(self):
        """
        ``True`` if this is the overdue interval, otherwise ``False``.

        """
        return self.start is None


    def add(self, bug):
        """
        Add given bug to this interval.

        Raises ``ValueError`` if the bug's deadline falls outside this
        interval.

        """
        if bug.deadline <= self.end and (
                self.start is None or bug.deadline >= self.start):
            day = self._by_deadline.setdefault(bug.deadline, Day(bug.deadline))
            day.add(bug)
            return super(Interval, self).add(bug)
        else:
            raise ValueError(
                "Bug deadline %s is outside interval %s to %s"
                % (bug.deadline, self.start, self.end))
