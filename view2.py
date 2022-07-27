# Flaskを利用するのでインポート
from flask import Flask, render_template,Blueprint
from flask_bootstrap import Bootstrap

bp2 = Blueprint('view2', __name__, url_prefix='/prc')

@bp2.route("/")
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)