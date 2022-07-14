# Flaskを利用するのでインポート
from flask import Flask, render_template,Blueprint
from flask_bootstrap import Bootstrap

bp = Blueprint('view2', __name__, url_prefix='/<name>')

@bp.route("/")
def hello(name):
    return render_template('hello.html', title='呼び出し側でタイトル設定', name=name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)