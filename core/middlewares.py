from stackexchange import StackOverflow
from .utils import render
from datetime import datetime
import os


class StackOverflowMiddleware(object):

    def process_exception(self, request, exception):
        so = StackOverflow()
        intitle = '{}'.format(exception.__class__.__name__)
        questions = so.search(intitle=intitle, tags=['python3', 'python'])
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ DEBUG @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print('Exception: {0}'.format(intitle))
        if len(questions):
            print('StockOverflow related questions:')
            print("<===================================================================>")
            for i, que in enumerate(questions):
                if i < 3:
                    print("{0}".format(que.title))
                    print("{0}".format(que.url))
                    print("<===================================================================>")
                else:
                    break
        else:
            print("No releated questions found")
        return render(400, template='templates/error.html',
                      context={'error_message': 'Exception Occured'})


class LogToConsole(object):

    def process_request(self, request):
        log = '[{time}] [{process}] [INFO] Request: /{url_path}'.format(
            time=datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %z'),
            process=os.getpid(),
            url_path=request.path_info
        )
        print(log)

    def process_response(self, request, response):
        log = '[{time}] [{process}] [INFO] Response: /{url_path} {status}'.format(
            time=datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %z'),
            process=os.getpid(),
            url_path=request.path_info,
            status=response.status_string
        )
        print(log)
