# Flaskを利用するのでインポート
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Flaskのインスタンスを生成
app = Flask(__name__)
bootstrap = Bootstrap(app)

# 「http://localhost:8000/」にアクセスしたら「index()を実行する」という意味
@app.route('/')
def index():
    return render_template('index.html')

# 「http://localhost:8000/○○」にアクセスしたら「hello(name)を実行する」という意味
# 「hello.html」ファイルにパラメータ2つを渡している
# name→URLで指定された○○の部分の文字列
@app.route('/<name>')
def hello(name):
    return render_template('hello.html', title='呼び出し側でタイトル設定', name=name)

@app.route("/bs")
def degign_bs():
    return render_template("bootstrap.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)