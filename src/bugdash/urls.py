from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    "bugdash.views",
    url("^$", "home", name="home"),
)
