
class HTTPResponse(object):

    def __init__(self, status=400, body={}):
        self.headers = {}
        self.body = body
        self.status_code = status

    @property
    def status_string(self):
        if self.status_code == 200:
            return '200 OK'
        elif self.status_code == 400:
            return '400 Bad Request'
        elif self.status_code == 404:
            return '404 Not Found'
        else:
            return '400 Bad Request'
