import os.path

from django.conf import settings

from bugzilla.agents import BugzillaAgent
from bugzilla.models import BugSearch
from bugzilla.utils import urljoin
from httplib2 import Http
from remoteobjects import fields

from .bugs import DashBug



class DashboardAgent(BugzillaAgent):
    def __init__(self, username=None, password=None):
        http = Http(ca_certs=settings.BUGZILLA_API_SSL_CA_CERT)
        super(DashboardAgent, self).__init__(
            settings.BUGZILLA_API_ROOT,
            username=username, password=password, http=http)


    def get_bugs(self, **kwargs):
        url = urljoin(self.API_ROOT, 'bug/?%s' % (self.qs(**kwargs)))
        return DashBugSearch.get(url, http=self.http).bugs



class DashBugSearch(BugSearch):
    bugs = fields.List(fields.Object(DashBug))
