# """FlaskのConfigを提供する"""
import os


class SystemConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'misato',
        'password': 'password',
        'host': 'localhost',
        'db_name':'todo'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


Config = SystemConfig