# -*- coding: utf-8 -*-

from flask import render_template

from flask_mail import Mail

from init_app import *


mail = Mail(app)                                # Initialize Flask-Mail

from models.models import *


def register_blueprints(this):
    from views.user_views import user_bp
    from views.post_views import post_bp

    this.register_blueprint(post_bp)
    this.register_blueprint(user_bp)


register_blueprints(app)
db.create_all()
db.session.commit()


@app.route('/')
def home_page():
    return render_template('home.html')

# Start development web server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
