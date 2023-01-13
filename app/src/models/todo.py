from datetime import datetime
from database import db

class Todo(db.Model):
  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255))
  #state = db.Column(db.String(255), nullable=False , primary_key=True)

  createTime = db.Column(db.DateTime, nullable=False, default=datetime.now , primary_key=True)
  updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, primary_key=True)

  def __repr__(self):
      return '<Todo id={id} name={name}>'.format(
              id=self.id, name=self.name)