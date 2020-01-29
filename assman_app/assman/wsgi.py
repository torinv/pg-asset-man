"""
WSGI config for assman project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# stuff from stack overflow
path = '/opt/python/current/app/assman_app'
if path not in sys.path:
	sys.path.append(path)

# Default stuff
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assman.settings')

application = get_wsgi_application()
