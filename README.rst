django-heroku
=============

This is a Django library for Heroku applications that ensures a seamless deployment and development experience.

This library provides:

-  Settings configuration (Static files / WhiteNoise).
-  Logging configuration.
-  Test runner (important for `Heroku CI <https://www.heroku.com/continuous-integration>`_).

--------------

Django 2.0 is targetted, but older versions of Django should be compatible.

Usage of Django-Heroku
----------------------

In ``settings.py``, at the very bottom

.. codeblock: python

    …
    # Configure Django App for Heroku.
    import django_heroku
    django_heroku.configure(locals())

This will automatically configure ``DATABASE_URL``, ``ALLOWED_HOSTS``, WhiteNoise (for static assets), Logging, and Heroku CI for your application.

**Bonus points!** If you set the ``SECRET_KEY`` environment variable, it will automatically be used in your Django settings, too!

✨🍰✨