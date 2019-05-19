from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permissions = db.Column(db.String(32), index=True)
    name = db.Column(db.String(32), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return f'<User {self.name}>'

        
class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    description = db.Column(db.String(128))
    
    def __repr__(self):
        return f'<Feed {self.timestamp} - {self.user_id}>'

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    translation = db.Column(db.String(32), index=True)
    
    def __repr__(self):
        return f'<Chapter {self.name} ({self.translation})>'

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    clip_id = db.Column(db.Integer, db.ForeignKey('clip.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)
    stars = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Review {self.timestamp} - {self.user_id}>'

class Clip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))
    reciter = db.Column(db.String(32))
    
    def __repr__(self):
        return f'<Clip {self.surah_id} - {self.reciter}>'

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    clip_id = db.Column(db.Integer, db.ForeignKey('clip.id'))
    positive = db.Column(db.Boolean)
    
    def __repr__(self):
        return f'<Vote {id}>'