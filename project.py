from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route('/test/redis')
def hello_world():


    return "works"


@app.route('/')
def hello_world():
    return 'Hello man!'


if __name__ == '__main__':
    app.run()
