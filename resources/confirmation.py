from flask import render_template, request, url_for, Response
from flask_restful import Resource
from libs.strings import gettext
from models.confirmation import ConfirmationModel


class Confirmation(Resource):
    @classmethod
    def get(cls, confirmation_id):
        link = request.url_root[:-1] + url_for("confirmation", confirmation_id=confirmation_id)
        return Response(render_template('user/confirmation.html', confirmation_id=confirmation_id, link=link))


    @classmethod
    def post(cls, confirmation_id):
        """Return confirmation HTML page."""
        confirmation = ConfirmationModel.find_by_id(confirmation_id)
        if not confirmation:
            return {"message": gettext("confirmation_not_found"), 'status': 404}

        if confirmation.expired:
            return {"message": gettext("confirmation_link_expired"), 'status': 404}

        if confirmation.confirmed:
            return {"message": gettext("confirmation_already_confirmed"), 'status': 404}

        confirmation.confirmed = True
        link = request.url_root[:-1] + url_for("confirmation", confirmation_id=confirmation_id)
        try:
            confirmation.save_to_db()
            ## LOGIN
            return {'email': confirmation.user.email, 'confirmation_id': confirmation_id, 'link': link, 'status': 200}
        except:
            confirmation.confirmed = False
            return {"message": gettext("confirmation_confirm_error"), 'status': 500}

