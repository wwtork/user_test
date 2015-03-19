from flask_user import UserMixin
from models.model import Model


class User(Model, UserMixin):
    def __init__(self, username, password, reset_password, email, confirmed_at, active, first_name, last_name):
        super(User, self).__init__()
        self.username = username
        self.password = password
        self.reset_password_token = reset_password
        self.email = email
        self.confirmed_at = confirmed_at
        self.active = active
        self.first_name = first_name
        self.last_name = last_name