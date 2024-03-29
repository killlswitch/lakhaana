from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from config import config
from flask.ext.login import LoginManager
from flask_wtf import CsrfProtect

login_manager = LoginManager()
mail = Mail()
bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
csrf = CsrfProtect()

login_manager.session_protection = 'basic'                    #strong should be in production build
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')
    return app
