from flask.ext.login import UserMixin
from . import login_manager, db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    dob = db.Column(db.Date(), default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Flask-Login integration
    def is_authenticated(self):
        return False

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    speciality = db.Column(db.String(64))
    menu_table = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<restaurant %r>' % self.name


class ChandniChonk(db.Model):
    __tablename__ = 'chandni_chock'
    id = db.Column(db.Integer, primary_key=True)
    reciepe = db.Column(db.String(64), index=True)
    cost = db.Column(db.Integer)

    def __repr__(self):
        return '<restaurant %r>' % self.name


class Apnadhaba(db.Model):
    __tablename__ = 'apna_dhaba'
    id = db.Column(db.Integer, primary_key=True)
    reciepe = db.Column(db.String(64), index=True)
    cost = db.Column(db.Integer)

    def __repr__(self):
        return '<restaurant %r>' % self.name


class ShootersCafe(db.Model):
    __tablename__ = 'shooters_cafe'
    id = db.Column(db.Integer, primary_key=True)
    reciepe = db.Column(db.String(64), index=True)
    cost = db.Column(db.Integer)

    def __repr__(self):
        return '<restaurant %r>' % self.name


class AnandMess(db.Model):
    __tablename__ = 'anand_mess'
    id = db.Column(db.Integer, primary_key=True)
    reciepe = db.Column(db.String(64), index=True)
    cost = db.Column(db.Integer)

    def __repr__(self):
        return '<restaurant %r>' % self.name


class PunjabiDhaba(db.Model):
    __tablename__ = 'punjabi_dhaba'
    id = db.Column(db.Integer, primary_key=True)
    reciepe = db.Column(db.String(64), index=True)
    cost = db.Column(db.Integer)

    def __repr__(self):
        return '<restaurant %r>' % self.name


class TomsDiner(db.Model):
    __tablename__ = 'toms_diner'
    id = db.Column(db.Integer, primary_key=True)
    reciepe = db.Column(db.String(64), index=True)
    cost = db.Column(db.Integer)

    def __repr__(self):
        return '<restaurant %r>' % self.name


class TheValleyJunction(db.Model):
    __tablename__ = 'the_valley_junction'
    id = db.Column(db.Integer, primary_key=True)
    reciepe = db.Column(db.String(64), index=True)
    cost = db.Column(db.Integer)

    def __repr__(self):
        return '<restaurant %r>' % self.name


class ChinaValley(db.Model):
    __tablename__ = 'china_valley'
    id = db.Column(db.Integer, primary_key=True)
    reciepe = db.Column(db.String(64), index=True)
    cost = db.Column(db.Integer)

    def __repr__(self):
        return '<restaurant %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
