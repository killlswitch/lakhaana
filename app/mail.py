from flask import render_template
from manage import app
from flask.ext.mail import Message


def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config.from_object['LAKHAANA_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config.from_object['LAKHAANA_MAIL_SENDER'], recipient=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
