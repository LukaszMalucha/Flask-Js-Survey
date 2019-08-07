import os
import env
from flask import request, url_for
from requests import Response
from models.confirmation import ConfirmationModel
from db import db
from libs.mailgun import Mailgun
from flask_login import UserMixin


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    confirmation = db.relationship("ConfirmationModel",
                                   lazy="dynamic",  # allows attaching confirmation to the user created previously
                                   cascade="all, delete-orphan")

    @property
    def most_recent_confirmation(self) -> "ConfirmationModel":
        """get most recent confirmation that belongs to the user"""
        return self.confirmation.order_by(db.desc(ConfirmationModel.expire_at)).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def send_confirmation_email(self) -> Response:
        # remove end slash from http://127.0.0.1:5000 + /user_confirm/1
        link = request.url_root[:-1] + url_for("confirmation", confirmation_id=self.most_recent_confirmation.id)
        subject = "Registration confirmation"
        text = f"Please click the link to confirm your registration: {link}"
        html = f'<html>Please click the link to confirm your registration: <a href="{link}">{link}</a></html>'
        return Mailgun.send_email([self.email], subject, text, html)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
