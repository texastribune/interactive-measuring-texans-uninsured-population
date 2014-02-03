import os

BASE_PATH = os.path.dirname(__file__)
file_name = lambda s: os.path.join(BASE_PATH, s)


def replace(a, contents):
    with open(file_name("%s.html" % a)) as f:
        contents = contents.replace("<!-- {{ %s here }} -->" % a, f.read())
    return contents


def app(environ, start_response):
    with open(file_name("_template.html")) as f:
        contents = f.read()

    contents = replace("content", contents)
    contents = replace("scripts", contents)
    contents = replace("styles", contents)

    response_headers = [
        ('Content-type', 'text/html'),
        ('Content-length', len(contents)),
    ]

    start_response("200 OK", response_headers)
    return iter([contents])
