#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template
from database import init_db,db
from models import Todo

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
        uebo = Todo(name='uebo')
        db.session.add(uebo)
        db.session.commit()
        return 'ueboを増やしました。'

    return app

app = create_app()

#おまじない
if __name__ == "__main__":
    app.run(debug=True)