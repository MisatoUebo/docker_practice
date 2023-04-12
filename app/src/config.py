# """FlaskのConfigを提供する"""
import os


class SystemConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'misato',
        'password': 'password',
        'host': '192.168.160.2',
        'db_name':'todo'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SECRET_KEY = b'\x98\xf5H\xb0\x90\xef\x8d\xc6\xcb\x12\x92\x19\x90or\xeb\xe0\x85F\xba$\x02\xd8.'


Config = SystemConfig