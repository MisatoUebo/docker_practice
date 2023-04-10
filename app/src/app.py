#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,redirect
from database import init_db,db
from models import Todo
from flask import request

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    init_db(app)

#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
    @app.route("/")
    def hello():
        return "Hello World"


#「/index」へアクセスがあった場合に、「index.html」を返す
    @app.route("/show")
    def show():
        users = Todo.query.all()
        return render_template('index.html',users=users)

    @app.route('/add')
    def add():
        return render_template('add.html')
        # uebo = Todo(name='uebo')
        # db.session.add(uebo)
        # db.session.commit()
        # return 'ueboを増やしました。'

    @app.route('/add', methods=['POST'])
    def postAdd():
        userData = request.form.get('userName') # hoge
        userName = Todo(name=userData)
        db.session.add(userName)
        db.session.commit()
        return '新規ユーザーを追加しました。'

    @app.route('/delete')
    def delete():
        users = Todo.query.all()
        return render_template('delete.html',users=users)

    @app.route('/delete', methods=['POST'])
    def postDelete():
        userData = request.form.get('id') 
        record_to_delete = db.session.query(Todo).filter_by(id=userData).first()

        if record_to_delete is not None:
            db.session.delete(record_to_delete)
            db.session.commit()
            return f'ID:{userData}を削除しました'
        else:
            return '該当するデータはありません'

    @app.route("/<int:id>/update",methods=["GET","POST"])
    def update(id):
        post = Todo.query.filter(Todo.id == id).first()
        if request.method == "GET":
            return render_template("update.html",post=post)
        
        else:
            post.name=request.form.get("name")
            db.session.commit()
            return redirect("/show")
    
    return app

app = create_app()

#おまじない
if __name__ == "__main__":
    app.run(debug=True)