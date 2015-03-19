from flask import Blueprint, render_template
from flask.views import MethodView

from models.models import User


user_bp = Blueprint('user', __name__, template_folder='templates')


class ListView(MethodView):

    def get(self):
        users = User.query.order_by('first_name')
        return render_template('user/list.html', users=users)


class ShowView(MethodView):

    def get(self, username):
        user = User.query.filter_by(username=username).first_or_404()
        return render_template('user/show.html', user=user)


# Register the urls
user_bp.add_url_rule('/user', view_func=ListView.as_view('list'))
user_bp.add_url_rule('/user/<username>/', view_func=ShowView.as_view('show'))