# coding: utf-8
"""
sql models

    use: Flask-SQLAlchemy
    -- http://flask-sqlalchemy.pocoo.org/2.1/

"""

from . import db

class Suan(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    direction=db.Column(db.Integer)
    relation=db.Column(db.Integer)
    result=db.Column(db.String(164))
    me=db.Column(db.String(164))

    def __repr__(self):
        return '<Suan %r>' % self.result


