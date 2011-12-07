from django.conf import settings
from django.utils.encoding import StrAndUnicode



class Area(StrAndUnicode):
    """
    A release readiness area (e.g. "security", "stability", "performance").

    An area that is listed in the ``BUGDASH_AREAS`` setting will have a
    numeric id that is its location in that list.

    An unknown area will have an id of 0.

    """
    def __init__(self, id_, name):
        self.id = id_
        self.name = name


    def __unicode__(self):
        return self.name


    def __repr__(self):
        return "Area(%r, %r)" % (self.id, self.name)



class AreaList(object):
    """
    A prioritized list of ``Areas``. Provides case-normalization and lookup
    conveniences around the ``BUGDASH_AREAS`` setting.

    """
    def __init__(self, area_names):
        """
        Create an ``AreaList`` given a list of area names.

        ``area_names`` is the list of known area names, in priority order, and
        cased as desired for display.

        """
        self.areas = []
        self._by_lc_name = {}
        self._by_id = {0: Area(0, "Unknown")}
        for id_, name in enumerate(area_names, 1):
            area = Area(id_, name)
            self.areas.append(area)
            self._by_lc_name[name.lower()] = area
            self._by_id[id_] = area


    def __iter__(self):
        """
        Iteration yields all known areas, followed by unknown area.

        """
        for area in self.areas:
            yield area
        yield self.unknown


    def by_id(self, id_):
        """
        Get an ``Area`` by its id.

        """
        return self._by_id[id_]


    def by_name(self, name):
        """
        Get an area by its (case-insensitive) name.

        Any name is valid; an unknown name will return a new ``Area`` with the
        given name and id 0.

        """
        return self._by_lc_name.get(name.lower(), Area(0, name))


    @property
    def unknown(self):
        """
        Shortcut for unknown area.

        """
        return self.by_id(0)



AREAS = AreaList(settings.BUGDASH_AREAS)
