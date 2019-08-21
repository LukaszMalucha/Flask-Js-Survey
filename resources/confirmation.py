from time import time

from flask import render_template, request, url_for, Response, session
from flask_restful import Resource
from flask_login import login_user
from libs.strings import gettext
from models.confirmation import ConfirmationModel


class ConfirmationPage(Resource):
    @classmethod
    def get(cls, confirmation_id):
        """User registration confirmation page"""
        link = request.url_root[:-1] + url_for("confirmationpage",
                                               confirmation_id=confirmation_id)  # create confirmation link
        confirmation = ConfirmationModel.find_by_id(confirmation_id)
        email = confirmation.user.email
        return Response(
            render_template('user/confirmation.html', confirmation_id=confirmation_id, link=link, email=email))


class Confirm(Resource):
    @classmethod
    def post(cls):
        """Confirm registration"""
        confirmation_data = request.get_json()
        confirmation_id = confirmation_data['confirmation_id']
        confirmation = ConfirmationModel.find_by_id(confirmation_id)
        if not confirmation:
            return {"message": gettext("confirmation_not_found"), 'status': 404}

        if confirmation.expired:
            return {"message": gettext("confirmation_link_expired"), 'status': 404}

        if confirmation.confirmed:
            return {"message": gettext("confirmation_already_confirmed"), 'status': 404}
        confirmation.confirmed = True
        try:
            confirmation.save_to_db()
            session['message_success'] = gettext("user_logged_in").format(confirmation.user.username)
            login_user(confirmation.user)
            return {'status': 200}
        except:
            confirmation.confirmed = False
            return {"message": gettext("confirmation_confirm_error"), 'status': 500}

