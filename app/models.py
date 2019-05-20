from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    permissions = db.Column(db.String(32), index=True)
    name = db.Column(db.String(32), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    
    def __repr__(self):
        return f'<User {self.id}>'

    def check_password(self, inp):
        return check_password_hash(self.password, inp)

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True)
    translation = db.Column(db.String(16), index=True)

    def __repr__(self):
        return f'<Chapter {self.id}>'

class Reciter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    nick = db.Column(db.String(16), index=True)

    def __repr__(self):
        return f'<Reciter {self.id}>'

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reciter = db.Column(db.Integer, db.ForeignKey('reciter.id'))
    chapter = db.Column(db.Integer, db.ForeignKey('chapter.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<Vote {self.id}>'