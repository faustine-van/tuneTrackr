#!/usr/bin/python3
"""set helper for email services"""
from flask_mail import Message
from api.v1.app import app
from api.v1.app import mail
from threading import Thread
from werkzeug.exceptions import InternalServerError


def send_async_email(app, msg):
    """send email"""
    with app.app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise InternalServerError("[MAIL SERVER] not working")


def send_email(subject, sender, recipients, text_body, html_body):
    "send email"
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()
