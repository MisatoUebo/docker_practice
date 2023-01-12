# ベースイメージ作成
FROM python:3.7

# requirements.txtをコピー
COPY requirements.txt .

# pipアップグレード
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 作業ディレクトリ指定
WORKDIR /workdir

# 公開ポート指定
EXPOSE 8000