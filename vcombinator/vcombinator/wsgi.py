"""
WSGI config for vcombinator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

path = '/opt/python/current/app/vcombinator'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "/vcombinator/vcombinator.settings")
print("**ME****ME************ME*******************ME*********ME*************ME**ME")

application = get_wsgi_application()
