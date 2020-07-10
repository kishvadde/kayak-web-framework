from cgi import parse_qs


class HTTPRequest(object):

    def __init__(self, environ):
        self.method = environ.get('REQUEST_METHOD', 'GET')
        self.headers = {}
        self.path_info = environ.get('PATH_INFO', '').lstrip('/')
        self.query_params = parse_qs(environ.get('QUERY_STRING', ''))

    @property
    def HEADERS(self):
        return self.headers
