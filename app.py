import os
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
def test():
    return template('<b>Hello, World</b>!')



port = int(os.environ.get('PORT', 5000))

run(host='0.0.0.0', port=port)
