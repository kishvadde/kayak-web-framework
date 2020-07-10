from .utils import render


def hello(request):
    if request.method == 'GET':
        return render(200, template='templates/hello.html',
                      context={'hello_message': 'Hola!, Amigo'})
    else:
        return render(400, template='templates/error.html',
                      context={'error_message': 'Bad request'})


def bye(request):
    if request.method == 'GET':
        return render(200, template='templates/bye.html',
                      context={'bye_message': 'Adios, Amigo!!!'})
    else:
        return render(400, template='templates/error.html',
                      context={'error_message': 'Bad request'})


def raise_exception(request):
    if request.method == 'GET':
        d = {}
        key = d['no_key']
    return render(400, template='templates/error.html',
                  context={'error_message': 'Bad request'})