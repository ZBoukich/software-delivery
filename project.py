from flask import Flask

app = Flask(__name__)


@app.route('/test/redis')
def hello_world():
    return "testing after jenkins configured again again"


@app.route('/')
def boe():
    return 'Hello dman  !'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
