from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    Submit = SubmitField('Log In')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField\
    ('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Username must have only letter, ''numbers, dots or underscores')])
    dob = DateField('Date of birth', format='%d/%m/%Y', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Password must match')])
    password2 = PasswordField('Confrim Password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')
