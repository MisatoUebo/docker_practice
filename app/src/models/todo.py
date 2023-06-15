from datetime import datetime
from database import db
from sqlalchemy.dialects import postgresql as pg

class Todo(db.Model):
  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  # name = db.Column(db.String(255))
  body = db.Column(db.String(50))
  title = db.Column(db.String(300))
  image_url = db.Column(db.String(120))
  tags = db.Column(pg.ARRAY(db.String), nullable=False,default=False)
  #state = db.Column(db.String(255), nullable=False , primary_key=True)

  createTime = db.Column(db.DateTime, nullable=False, default=datetime.now , primary_key=True)
  updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, primary_key=True)

  def __repr__(self):
      return '<Todo id={id} name={name}>'.format(
              id=self.id, body=self.body, image_url=self.image_url, title=self.title)