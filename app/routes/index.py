from flask import (
  Blueprint,
  render_template,
  current_app as app
)

bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("")
@bp.route("<path:path>")
def get_index(path=None):
  # return app.send_static_file('index.html')
  return render_template("index.html")
