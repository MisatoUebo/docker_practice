#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,redirect,flash
from database import init_db,db
from models import Todo
from flask import request

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    init_db(app)

#「/」へアクセスがあった場合に、「index.html」を返す
    @app.route("/")
    def show():
        users = Todo.query.all()
        return render_template('index.html',pageTitle = "ユーザー一覧画面",users=users)

    @app.route('/add', methods=["GET","POST"])
    def add():
        if request.method == "GET":
            return render_template("add.html",pageTitle="ユーザー追加画面")
        else:
            title = request.form.get('title') # hoge
            body = request.form.get('body') # hoge
            userName = Todo(title=title , body=body)
            db.session.add(userName)
            db.session.commit()
            return redirect("/")

    @app.route('/delete', methods=["GET","POST"])
    def postDelete():

        if request.method == "GET":
            users = Todo.query.all()
            return render_template('delete.html',pageTitle="ユーザー削除画面",users=users)
        else:
            if request.form.get("id") == "":
                flash("削除したいIDを入力してください", "failed")
                users = Todo.query.all()

            if request.form.get("id"):
                userData = request.form.get('id') 
                record_to_delete = db.session.query(Todo).filter_by(id=userData).first()
                if record_to_delete is not None:
                    db.session.delete(record_to_delete)
                    db.session.commit()
                    flash(f'ID:{userData}を削除しました。', "success")
                else:
                    flash("該当するデータはありません", "failed")
                
                users = Todo.query.all()
            
            return render_template("delete.html",users=users)

    @app.route("/<int:id>/update",methods=["GET","POST"])
    def update(id):
        post = Todo.query.filter(Todo.id == id).first()
        if request.method == "GET":
            return render_template("update.html",pageTitle="ユーザー情報編集画面",post=post)
        
        else:
            post.title=request.form.get("title")
            db.session.commit()
            return redirect("/")
        
    @app.route("/<int:id>/contents",methods=["GET"])
    def showContents(id):
        post = Todo.query.filter(Todo.id == id).first()
        if request.method == "GET":
            return render_template("contents.html",pageTitle="内容",post=post)
    
    return app

app = create_app()

#おまじない
if __name__ == "__main__":
    app.run(debug=True)