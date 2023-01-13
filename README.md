## 操作手順
参考資料 : https://qiita.com/AndanteSysDes/items/a25acc1523fa674e7eda

### docker-compose 起動
1. ``dc build``
2. ``dc up -d``

### DBのホストを設定
3. ``docker network inspect my_flask_default``
4. dbのIPをconfig.pyのhost部分に記入

### migrateする
5. ``docker exec -it my_flask_flask_1 bash``
6. コンテナ内で以下の操作を行う
    ``flask db init``
    ``flask db migrate``
    ``flask db upgrade``

### MySQLコンテナに入る
7. ``docker exec -it my_flask_db_1 bin/bash``
8. コンテナ内で以下の操作を行う
    ``mysql -u misato -ppassword todo``
    ``mysql> show tables;``

### 実際にアクセスする
- localhost:5000/
  - サービスの概要説明、
- localhost:5000/add
  - ueboが増える