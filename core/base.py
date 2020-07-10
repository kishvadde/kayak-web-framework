from .urls import view_resolver
from .request import HTTPRequest
from .utils import render
from .middlewares import StackOverflowMiddleware, LogToConsole


def process_exception_middleware(request, e):
    somw_instance = StackOverflowMiddleware()
    return somw_instance.process_exception(request, e)


def process_request_middleware(request):
    mw_instance = LogToConsole()
    mw_instance.process_request(request)


def process_response_middleware(request, response):
    mw_instance = LogToConsole()
    mw_instance.process_response(request, response)


def handler(environ, start_response):
    request = HTTPRequest(environ)

    view = None
    try:
        process_request_middleware(request)
        view = view_resolver(request.path_info)
    except Exception as e:
        response = render(404, template='templates/error.html',
                          context={'error_message': 'No Page found'})
    if view:
        try:
            response = view(request)
        except Exception as e:
            response = process_exception_middleware(request, e)
    status = response.status_string
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response.body)))
    ]
    process_response_middleware(request, response)
    response = response.body.encode('ascii')
    start_response(status, headers)
    return iter([response])
