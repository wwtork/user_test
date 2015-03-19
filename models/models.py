import datetime
from flask_user import UserMixin
from init_app import db


class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        # User authentication information
        username = db.Column(db.String(50), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False, server_default='')
        reset_password_token = db.Column(db.String(100), nullable=False, server_default='')

        # User email information
        email = db.Column(db.String(255), nullable=False, unique=True)
        confirmed_at = db.Column(db.DateTime())

        # User information
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
        first_name = db.Column(db.String(100), nullable=False, server_default='')
        last_name = db.Column(db.String(100), nullable=False, server_default='')
        roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))
        comments = db.relationship('Comment')
        posts = db.relationship('Post')


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))


class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)

        title = db.Column(db.String(50))
        text = db.Column(db.Text)

        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        posted_at = db.Column(db.DateTime(), default=datetime.datetime.now, nullable=False)
        edited_at = db.Column(db.DateTime())
        comments = db.relationship('Comment')
        on_moderation = db.Column('on_moderation', db.Boolean(), nullable=False, server_default='0')


