from .base import handler


def app(environ, start_response):
        return handler(environ, start_response)
