from flask import make_response, render_template, request, url_for
from flask_restful import Resource
from libs.strings import gettext
from models.confirmation import ConfirmationModel
from schemas.confirmation import ConfirmationSchema

confirmation_schema = ConfirmationSchema()


class Confirmation(Resource):
    @classmethod
    def get(cls, confirmation_id):
        """Return confrimation HTML page."""
        confirmation = ConfirmationModel.find_by_id(confirmation_id)
        if not confirmation:
            return {"message": gettext("confirmation_not_found")}, 404

        if confirmation.expired:
            return {"message": gettext("confirmation_link_expired")}, 404

        if confirmation.confirmed:
            return {"message": gettext("confirmation_already_confirmed")}, 404

        confirmation.confirmed = True
        confirmation.save_to_db()

        headers = {"Content-Type": "text/html"}
        return make_response(render_template("user/confirmation_page.html", email=confirmation.user.email), 200, headers)


class ConfirmationEmail(Resource):
    @classmethod
    def get(cls, confirmation_id):
        link = request.url_root[:-1] + url_for("confirmation", confirmation_id=confirmation_id)
        return make_response(render_template("user/confirmation_email.html", link=link, confirmation_id=confirmation_id))


