from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template


urlpatterns = patterns(
    "",
    url("^$",
        direct_to_template,
        {"template": "home.html"},
        name="home"),
)
