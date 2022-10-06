# Flaskを利用するのでインポート
from flask import Flask,render_template,request,redirect
from flask_bootstrap import Bootstrap
# SQLAlchemyをインポート
from flask_sqlalchemy import SQLAlchemy
import os

# base_dir = os.path.dirname(__file__)  # このmodel.pyを配置しているディレクトリのパス

from view1 import bp
from view2 import bp2

# Flaskのインスタンスを生成
app = Flask(__name__)

bootstrap = Bootstrap(app)
app.register_blueprint(bp)
app.register_blueprint(bp2)

# SQLALCHEMY_DATABASE_URIではデータベースを作成する為にデータベースの種類とファイル名を書いています。
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
# SQLALCHEMY_TRACK_MODIFICATIONSではデータベースでイベントシステムがSQLAlchemyのセッションへの変更を追跡します。
# と書いてありましたが無効にする事でリソース（メモリなど）の節約になるみたいです、よく分からないのもあるし無効でいきましょう。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# QL文等のログを出力してくれます。
app.config['SQLALCHEMY_ECHO'] = True
# db = SQLAlchemy(app)でSQLAlchemyのインスタンスを作成して変数dbに割り当てています。
db = SQLAlchemy(app)

# class ToDo(db.Model):で、dbのModelを継承したテーブルのクラスを定義しています。
# idの部分でprimary_key=Trueにしているのは、このidというのを主キーとして作成するよ、という指定です。
# データベースの中で同じ値のものがあっても区別ができるように一意のデータを各レコード（行）に持たせておかないといけないので、このidというデータにその役割を持たせています。
class ToDo(db.Model):
    __tablename__ = 'ToDo'
    id = db.Column(db.Integer,primary_key=True)
    todo = db.Column(db.String(128),nullable=False)
    date = db.Column(db.String)

@app.before_first_request
def init():
    db.create_all()

# 「http://localhost:8000/」にアクセスしたら「index()を実行する」という意味
@app.route('/', methods=["GET"])
def index():
    # GET送信の処理
    datas = ToDo.query.all()

    # last_name = request.args.get("last_name","")
    # first_name = request.args.get("first_name","")
    return render_template('index.html', lists = datas)

@app.route('/result', methods=["POST"])
def result_post():
    # POST送信の処理
    todo_txt = request.form["todo"]
    date_txt = request.form["date"]

    todos = ToDo(todo = todo_txt, date = date_txt)

    db.session.add(todos)
    db.session.commit()

    return redirect('/')
    # return render_template('result.html', last_name=last_name, first_name=first_name)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)