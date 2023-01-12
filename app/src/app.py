#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template
from database import init_db,db
from models import Todo
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate  # 追加

#Flaskオブジェクトの生成
#app = Flask(__name__)

#db = SQLAlchemy()
#migrate = Migrate(app, db)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    init_db(app)

#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
# @app.route("/")
# def hello():
#     return "Hello World"


#「/index」へアクセスがあった場合に、「index.html」を返す
    @app.route("/index")
    def index():
        '''
        res = db.session.query(Todo).all()
        for user in res:
            return render_template('index.html',user=user)
        '''

        return "indexのページ"
        
    return app

app = create_app()

#おまじない
if __name__ == "__main__":
    app.run(debug=True)



# def create_app():
#   app = Flask(__name__)
#   app.config.from_object('src.config.Config')

#   init_db(app)

#   return app


# app = create_app()