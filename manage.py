#!/usr/bin/env python

"""Django's manage.py."""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    from django.conf import settings

    if settings.DEBUG:
        if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
            import ptvsd
            ptvsd.enable_attach(address=('0.0.0.0', 3000), redirect_output=True)

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

        raise

    # This allows easy placement of apps within the interior
    # apps directory.
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, ".."))
    sys.path.append(os.path.join(current_path, "apps"))

    execute_from_command_line(sys.argv)
