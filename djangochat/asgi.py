"""
ASGI config for djangochat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import django

django.setup()

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from djangochat.environment import DAPHNE_FOR_HTTP
from room import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

protocol_mapping = {
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    )
}

# If in LOCAL environment, it adds http handler
if DAPHNE_FOR_HTTP:
    protocol_mapping['http'] = get_asgi_application()

# Creates the ProtocolTypeRouter with its mapping
application = ProtocolTypeRouter(protocol_mapping)
