from flask import Flask

app = Flask(__name__)


@app.route('/test/redis')
def hello_world():


    return "works"


@app.route('/')
def boe():
    return 'Hello man!'


if __name__ == '__main__':
    app.run()
