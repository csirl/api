from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


socketio.init_app(app, cors_allowed_origins="*")


@socketio.on('broadcast', namespace='/csirl')
def test_message(message):
    print(f'Broadcast: {message}')
    emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('connect', namespace='/csirl')
def test_connect():
    print('Client connected.')
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/csirl')
def test_disconnect():
    print('Client disconnected.')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)