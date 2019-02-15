"""
WSGI config

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from app.config import get_project_root_path, import_env_vars

import_env_vars(os.path.join(get_project_root_path(), 'envdir'))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.config.settings.heroku")


application = get_wsgi_application()
