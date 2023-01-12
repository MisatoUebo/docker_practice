# """FlaskのConfigを提供する"""
import os


class SystemConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8'.format(**{
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'port': 3306,
        'db_name':'todo'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


Config = SystemConfig