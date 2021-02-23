import os
import dotenv

from flask import Flask, url_for
from flask_cors import CORS

from app.routes import init_routes

APP_PATH = os.path.abspath(os.path.dirname(__file__))

# For reload changed static file.
def dated_url_for(endpoint, **values):
  from flask import current_app as app
  if endpoint == 'static':
    filename = values.get('filename', None)
    if filename:
      file_path = os.path.join(app.static_folder, filename)
      values['q'] = int(os.stat(file_path).st_mtime)
  return url_for(endpoint, **values)

def create_app():
  dotenv.load_dotenv(dotenv_path=".env")
  
  app = Flask(
    __name__,
    static_url_path = "/static/",
    static_folder = os.path.join(APP_PATH, "src"),
    template_folder = os.path.join(APP_PATH, "src")
  )
  app.url_map.strict_slashes = False
  
  FLASK_ENV = os.environ.get("FLASK_ENV", "production").lower()
  if FLASK_ENV == "development":
    app.config.from_object("app.config.DevelopmentConfig")
  else:
    app.config.from_object("app.config.ProductionConfig")
  
  SECRET_KEY = app.config.get("SECRET_KEY") or os.environ.get("SECRET_KEY", None)
  if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")
  app.config["SECRET_KEY"] = SECRET_KEY
  
  @app.context_processor
  def override_url_for():
    return dict(url_for=dated_url_for)
  
  with app.app_context():
    CORS(
      app=app,
      resources={ r"*": { "origin": "*" } }
    )
    init_routes()
    
  return app