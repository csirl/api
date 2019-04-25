from flask import Flask, Response
from flask_restplus import Api
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)

@app.route('/')
def index():
    return "OK"

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)