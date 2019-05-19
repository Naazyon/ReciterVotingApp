from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permissions = db.Column()
    name = db.Column()
    email = db.Column()
    password_hash = db.Column()
    online = db.Column()
    numVotes = db.Column()
    numReviews = db.Column()
    
    def __repr__(self):
        return f'<User {self.name}>'