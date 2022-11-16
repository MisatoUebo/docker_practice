# python 3.6 をベースにDockerイメージを作成
FROM python:3.6

# 作業ディレクトリを指定
WORKDIR /app

# カレントディレクトリのファイルをDockerコンテナの｢/app｣ ディレクトリにコピー
ADD . /app

# Flaskをインストール
RUN pip install Flask

# 外部に公開するポートを指定
EXPOSE 8000

# コンテナの実行コマンドを指定
CMD ["python", "app.py"]

RUN pip install flask-bootstrap4
RUN pip install flask-sqlalchemy
RUN pip install SQLAlchemy
RUN pip install mysql
RUN pip install mysqlclient
RUN pip install pymysql