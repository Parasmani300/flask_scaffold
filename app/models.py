from app import db

class Contact(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    city = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phonenum = db.Column(db.String())
    userid = db.Column(db.Integer(),db.ForeignKey('user.id'),nullable=False)

class User(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    contact = db.relationship(
        'Contact',
        backref='user',
        lazy=True,
        uselist=False)
    
    def __init__(self,username):
        self.username = username
    
    def __repr__(self):
        return '<User: ' + self.username +'>'
