Bugzilla Dashboard
==================

A "release readiness" and work prioritization dashboard for Bugzilla users.

Development
-----------

If you want to run this project in a `virtualenv`_ to isolate it from
other Python projects on your system, create a virtualenv and activate
it.  Then run ``bin/install-reqs`` to install the dependencies for
this project into your Python environment.

You'll probably need to create a ``src/bugdash/settings/local.py`` file with
some details of your local configuration.  See
``src/bugdash/settings/local.sample.py`` for a sample that can be copied to
``src/bugdash/settings/local.py`` and modified.

Once this configuration is done, you should be able to run ``./manage.py
runserver`` and access the site in your browser at
``http://localhost:8000``.

.. _virtualenv: http://www.virtualenv.org

To install the necessary Ruby gems for Compass/Sass development (only
necessary if you plan to modify Sass files and re-generate CSS), run
``bin/install-gems``.  Update ``requirements/gems.txt`` if newer gems should
be used.

Deployment
----------

When deployed under a multi-process webserver, a real cache backend must be
configured in place of the default "local memory" cache - see the ``CACHES``
setting in ``src/bugdash/settings/local.sample.py``.

In addition to the above configuration, in any production deployment
this entire app should be served exclusively over HTTPS (since serving
authenticated pages over HTTP invites session hijacking
attacks). Ideally, the non-HTTP URLs should redirect to the HTTPS
version.

``src/bugdash/settings/prod.py`` should be used as the settings module in a
production deployment in place of ``src/bugdash/settings/default.py`` (set
``DJANGO_SETTINGS_MODULE=bugdash.settings.prod``). Site-specific overrides
can still be placed in ``src/bugdash/settings/local.py``.

You can run ``./manage.py checksecure`` to verify that settings are correctly
configured for a secure deployment.

This app also uses the `staticfiles contrib app`_ in Django 1.3 for collecting
static assets from reusable components into a single directory for production
serving.  Under "runserver" in development this is handled automatically.  In
production, run ``./manage.py collectstatic`` followed by ``./manage.py
compress`` to collect and compress all static assets into the
``collected-assets`` directory (or whatever ``STATIC_ROOT`` is set to in
``src/bugdash/settings/local.py``), and make those collected assets available
by HTTP at the ``STATIC_URL`` setting.

.. _staticfiles contrib app: http://docs.djangoproject.com/en/1.3/howto/static-files/
