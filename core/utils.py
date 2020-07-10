import os
from .response import HTTPResponse


def render(status, template, context={}):

    html = None
    dir_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(dir_path, template)
    try:
        with open(template_path, 'r') as template:
            html_content = template.read()
            html = html_content.format(**context)
    except Exception as e:
        html = """<html>
                    <head>
                    <head>
                    <body>
                        <div style="background-color:red;position:absolute;left:50%;top:50%;width:30em;height:18em;">
                            <h2>No Page Found</h2>
                        </div>
                    </body>
                  </html>"""
    return HTTPResponse(status, html)
