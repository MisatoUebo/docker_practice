#!/bin/sh

#マウントしたmysqlのデータフォルダ削除
cd mysql
rm -drf mysql_data

#logsファイル内削除
cd logs
rm -rf *

cd ../../

#python実行時のキャッシュ削除
cd app/src
rm -drf __pycache__
rm -drf migrations

cd models
rm -drf __pycache__

# # 1/14 追記 : 固定IP化したので不必要になった

# #config.pyの中身の一部を修正
# cd ../
# sed -i -e "s/'host': '.*'/'host': 'localhost'/" config.py

# #config.pyの中身を書き換えた後のいらないデータ削除
# rm -f config.py-e
