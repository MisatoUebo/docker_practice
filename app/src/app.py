#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,redirect,flash
from database import init_db,db
from models import Todo
from flask import request

# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
from sqlalchemy import desc
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # 画像のアップロード先のディレクトリ
    UPLOAD_FOLDER = './static/image'
    # 画像を表示する際の参照元ディレクトリ
    DISPLAY_FOLDER = '/static/image'
    # アップロードされる拡張子の制限
    ALLOWED_EXTENSIONS = set(["png", "jpg", "gif"])

    tagList = []

    init_db(app)

#「/」へアクセスがあった場合に、「index.html」を返す
    @app.route("/")
    def show():
        users = Todo.query.all()
        todos = Todo.query.order_by(desc(Todo.createTime))
        tags = list(set([todo.tag for todo in todos]))
        return render_template("index.html",pageTitle = "ブログ一覧",users=users,tags=tags)
        #return render_template("index.html",pageTitle = "ブログ一覧",users=users)


    @app.route("/add", methods=["GET","POST"])
    def add():
        # "GET"の時
        if request.method == "GET":
            return render_template("add.html",pageTitle="ブログ記事作成")
        # "POST"の時
        elif request.method == "POST":
            title = request.form.get("title")
            body = request.form.get("body")
            tag = request.form.get("add-tag")

            # ファイルがなかった場合の処理
            if "file" not in request.files:
                filename = "No selected file"
                userData = Todo(title=title , body=body,image_url=filename,tag=tag)

                db.session.add(userData)
                db.session.commit()
                return redirect("/")
            
            # データの取り出し
            file = request.files["file"]

            if file.filename == '':
                filename = "No selected file"
                userData = Todo(title=title , body=body,image_url=filename,tag=tag)
            
                db.session.add(userData)
                db.session.commit()
                return redirect("/")

            if file and allwed_file(file.filename):
                # 危険な文字を削除（サニタイズ処理）
                filename = secure_filename(file.filename)
                # ファイルの保存
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            
                userData = Todo(title=title , body=body,image_url=filename,tag=tag)
            
                db.session.add(userData)
                db.session.commit()
                return redirect("/")
            


    @app.route("/delete", methods=["GET","POST"])
    def postDelete():

        if request.method == "GET":
            users = Todo.query.all()
            return render_template("delete.html",pageTitle="ブログ記事削除",users=users)
        else:
            if request.form.get("id") == "":
                flash("削除したいIDを入力してください", "failed")
                users = Todo.query.all()

            if request.form.get("id"):
                userData = request.form.get("id") 
                record_to_delete = db.session.query(Todo).filter_by(id=userData).first()
                if record_to_delete is not None:
                    db.session.delete(record_to_delete)
                    db.session.commit()
                    flash(f"ID:{userData}を削除しました。", "success")
                else:
                    flash("該当するデータはありません", "failed")
                
                users = Todo.query.all()
            
            return render_template("delete.html",users=users)

    @app.route("/<int:id>/update",methods=["GET","POST"])
    def update(id):
        post = Todo.query.filter(Todo.id == id).first()
        if request.method == "GET":
            return render_template("update.html",pageTitle="ブログ記事編集",post=post)
        
        else:
            post.title=request.form.get("title")
            post.body=request.form.get("body")
            db.session.commit()
            return redirect("/")
        
    @app.route("/<int:id>/contents",methods=["GET"])
    def showContents(id):
        post = Todo.query.filter(Todo.id == id).first()
        post.image_url = os.path.join(DISPLAY_FOLDER, post.image_url)
        if request.method == "GET":
            return render_template("contents.html",pageTitle="内容",post=post)
    
    def allwed_file(filename):
        # .があるかどうかのチェックと、拡張子の確認
        # OKなら１、だめなら0
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    
    return app

app = create_app()

#おまじない
if __name__ == "__main__":
    app.run(debug=True)