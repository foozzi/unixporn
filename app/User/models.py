from app.db import db
from werkzeug.security import generate_password_hash, \
     check_password_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return '<User %r>' % self.email
