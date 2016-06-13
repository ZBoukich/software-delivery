from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)



@app.route('/test/redis')
def hello_world():
    visits=redis.incr('counter',2)
    html= "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}<br/>"
    return html.format(name=os.getenv('NAME', "world"), hostname=socket.gethostname(), visits=visits)


@app.route('/')
def hello_world():
    return 'Hello man!'


if __name__ == '__main__':
    app.run()
