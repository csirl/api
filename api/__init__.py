import json

from flask import Flask, abort
from flask_socketio import SocketIO

if __name__ == '__main__':
    socketio.run(app)


# def create_app(test_config=None):
#     app = Flask(__name__)
#     app.config.from_pyfile('config.py')
#     socketio = SocketIO(app)

#     @app.route('/')
#     def index():
#         return '', 200

#     @app.route('/ping')
#     def ping():
#         return '', 200

#     return app