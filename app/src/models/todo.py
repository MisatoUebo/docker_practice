#from datetime import datetime
from database import db

class Todo(db.Model):
  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  #state = db.Column(db.String(255), nullable=False , primary_key=True)

  # createTime = db.Column(db.DateTime, nullable=False, default=datetime.now , primary_key=True)
  # updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, primary_key=True)

""" 
  def __repr__(self):
      return '<User id={id} name={name}>'.format(
              id=self.id, name=self.name)



  def __repr__(self):
    return '<TodoModel {}:{}>'.format(self.id, self.name) """