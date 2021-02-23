class BaseConfig(object):
  TESTING = False
  SECRET_KEY = "Dochi's upbit"
  JSONIFY_PRETTYPRINT_REGULAR = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
class ProductionConfig(BaseConfig):
  # SQLALCHEMY_SQLITE_URI="sqlite:///app/example.db"
  pass

class DevelopmentConfig(BaseConfig):
  # SQLALCHEMY_SQLITE_URI="sqlite:///app/example.db"
  pass

class TestingConfig(BaseConfig):
  TESTING = True
