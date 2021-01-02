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
        'Blogpost',
        backref='user',
        lazy='dynamic')
    
    def __init__(self,username):
        self.username = username
    
    def __repr__(self):
        return '<User: ' + self.username +'>'

class Blogpost(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(300))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    userid = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Blogpost '{}'>".format(self.title)
