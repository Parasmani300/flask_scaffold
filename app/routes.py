from flask import redirect
from app import app,db
from .models import User,Contact

@app.route('/')
def index():
    # try:
    #     # db.create_all()
    # db.create_all()
    # user1 = User(username="Paras")
    # user2 = User(username="Mani")
    # db.session.add(user1)
    # db.session.add(user2)
    # db.session.commit()

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
    return "Hi"