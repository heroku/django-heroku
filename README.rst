django-heroku
=============

This is a (work in progress) Django library for Heroku apps.

It could serve many purposes, including (but not limited to):

-  Settings configuration (static files / whitenoise)
-  Logging configuration (currently not covered at all)
-  Test runner (important for CI)
-  Potentially, starter template (hard to maintain)
-  Potentially, gunicorn runner (prob not neccessary)

It will depend on the following libraries:

-  dj-database-url (or django-environ)
-  psycopg2
-  WhiteNoise
-  Gunicorn, potentially

--------------

Django 2.0 will be targetted.

The name of the library is pretty set, but still to–be–determined.

Possible Usage
--------------

In ``settings.py``:

::

    …
    # Configure Django App for Heroku.
    django_heroku.configure(locals())
