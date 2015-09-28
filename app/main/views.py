from flask import render_template, abort
from . import main
from flask.ext.login import login_required
from ..models import User, Restaurant


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('main/user.html', user=user)


@main.route('/user/list')
@login_required
def list():
    restaurants = Restaurant.query.order_by(Restaurant.name).all()
    render_template('main/list.html', restaurants=restaurants)
