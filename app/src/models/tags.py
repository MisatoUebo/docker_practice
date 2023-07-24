from datetime import datetime
from database import db
from sqlalchemy.dialects import postgresql as pg

class Tag(db.Model):
  __tablename__ = 'tags'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  tag = db.Column(db.String(100))

  def __repr__(self):
      return '<Todo id={id} tag={tag}>'.format(
              id=self.id, tag=self.tag)