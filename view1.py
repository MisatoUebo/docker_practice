# Flaskを利用するのでインポート
from flask import Flask, render_template,Blueprint
from flask_bootstrap import Bootstrap

bp = Blueprint('view1', __name__, url_prefix='/bs')

@bp.route("/")
def degign_bs():
    return render_template("bootstrap.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)