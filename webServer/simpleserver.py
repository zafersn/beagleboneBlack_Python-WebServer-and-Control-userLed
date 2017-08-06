from bottle import route, run, template


@route('/')
@route('/<name>')
def index(name='World'):
    return template('hello_template', name=name)

run(host='0.0.0.0', port=8080)
