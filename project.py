from flask import Flask

app = Flask(__name__)


@app.route('/test/redis')
def hello_world():
    return "test a commit"


@app.route('/')
def boe():
    return 'Hello man!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
