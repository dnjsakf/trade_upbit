from flask_script import Manager
from socketio import WSGIApp

from app import create_app
from sockets import create_sio

app = create_app()
sio = create_sio()
manager = Manager(app)

@manager.command
@manager.option('-h', '--host', help='Host')
@manager.option('-p', '--port', help='Port')
def run(host="localhost", port=3000):
  app.wsgi_app = WSGIApp(sio, app.wsgi_app)
  app.run(host=host, port=int(port), threaded=True)

if __name__ == '__main__':
  manager.run()
