from flask import render_template, abort, redirect, url_for, session
from . import main
from .forms import Number
from flask.ext.login import login_required
from ..models import User, Restaurant, Menu


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
    return render_template('main/list.html', restaurants=restaurants)


@main.route('/user/<int:id>', methods=['GET', 'POST'])
@login_required
def menu(id):
    number = Number()
    restaurant = Restaurant.query.get_or_404(id)
    menu = restaurant.menu_table.all()
    menulist = Menu.query.get_or_404(id)
    number.amount.data = 1
    if number.validate_on_submit():
        multiplier = number.amount.data
        total = multiplier
        cart = []
        cart.append([menu, multiplier, total])
        return redirect(url_for('main.menu', restaurant=restaurant.name, menu=menu, form=number))
    return render_template('main/menu.html', restaurant=restaurant.name, menu=menu, form=number, cart=[])
