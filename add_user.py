from init_app import db
from models.models import User, Post

u1 = User.query.filter_by(username='wwtork1').first_or_404()
u2 = User.query.filter_by(username='wwtork2').first_or_404()

db.session.commit()

p1 = Post(title='post1', text='text text text', user_id=u1.id)
p2 = Post(title='post2', text='text text text', user_id=u1.id)
p3 = Post(title='post3', text='text text text', user_id=u2.id)
p4 = Post(title='post4', text='text text text', user_id=u2.id)


db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)

db.session.commit()