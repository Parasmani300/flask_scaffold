from flask import redirect
from app import app,db
from .models import User,Contact,Blogpost

@app.route('/')
def index():
    # try:
    #     # db.create_all()
    # db.create_all()
    

    # user1.contact = Contact(city='London', email='john.willy@xyz.com', phonenum='675-876-2423')
    # user2.contact = Contact(city='Chicago', email='fbaggin@abc.com', phonenum='563-983-7682')
    # db.session.add(user1)
    # db.session.add(user2)
    # db.session.commit()

    # print(User.query.all())
    # print('Hello')
    # print(Contact.query.all())
    # except Exception:
    #     db.create_all()
    #     # return redirect('/')
    db.create_all()
    user1 = User(username="Paras")
    user2 = User(username="Mani")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    users = User.query.all()

    post1 = Blogpost(title='Flask - A Python Web Framework')
    post2 = Blogpost(title='Using Templates in Flask')
    post3 = Blogpost(title='Working with Databases in Flask')
    post4 = Blogpost(title='RestAPI Programming in Flask')
    post1.userid = users[0].id
    post3.userid = users[0].id
    post4.userid = users[1].id
    post2.userid = users[1].id
    
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.commit()

    return "Hi"