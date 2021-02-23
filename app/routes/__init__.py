__all__ = [ "init_routes" ]

def init_routes():
  from flask import current_app as app
  
  from .index import bp as bp_index
  app.register_blueprint(bp_index, url_prefix="/")