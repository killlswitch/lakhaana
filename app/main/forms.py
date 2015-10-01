from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import Required


class Number(Form):
    amount = IntegerField("", validators=[Required()])
    submit = SubmitField("Add")