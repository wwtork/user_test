from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from wtforms.ext.sqlalchemy.orm import model_form

from models.models import Post, Comment
from init_app import db


post_bp = Blueprint('post', __name__, template_folder='templates')


class ListView(MethodView):

    def get(self):
        posts = Post.query.order_by('id')
        return render_template('post/list.html', posts=posts)


class ShowView(MethodView):
    form = model_form(Comment, exclude=['posted_at', 'edited_at'])

    def get_context(self, post_id):
        post = Post.query.filter_by(id=post_id).first_or_404()
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context

    def get(self, post_id):
        context = self.get_context(post_id)
        return render_template('post/show.html', **context)

    def post(self, post_id):
        context = self.get_context(post_id)
        form = context.get('form')

        if form.validate():
            comment = Comment()
            form.populate_obj(comment)

            post = context.get('post')
            post.comments.append(comment)
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('post.list', post_id=id))

        return render_template('post/list.html', **context)

# Register the urls
post_bp.add_url_rule('/post', view_func=ListView.as_view('list'))
post_bp.add_url_rule('/post/<post_id>/', view_func=ShowView.as_view('show'))