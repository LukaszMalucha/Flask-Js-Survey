import traceback
from flask import request, render_template, make_response
from flask_restful import Resource
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity, \
    jwt_required, get_raw_jwt
from marshmallow import ValidationError
from blacklist import BLACKLIST
from schemas.user import UserSchema
from libs.mailgun import MailGunException
from models.confirmation import ConfirmationModel
from libs.strings import gettext

user_schema = UserSchema()


class UserRegister(Resource):

    @classmethod
    def post(cls):
        user = user_schema.load(request.get_json())

        if UserModel.find_by_username(user.username):
            return {"message": gettext("user_username_exists")}, 400

        if UserModel.find_by_email(user.email):
            return {"message": gettext("user_email_exists")}, 400

        try:
            user.save_to_db()
            confirmation = ConfirmationModel(user.id)
            confirmation.save_to_db()
            user.send_confirmation_email()
            return {"message": gettext("user_registered")}, 201
        except MailGunException as e:
            user.delete_from_db()
            return {"message": str(e)}, 500
        except:  # user failed to save to db
            traceback.print_exc()
            user.delete_from_db()
            return {"message": gettext("user_error_creating")}, 500


class User(Resource):

    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': gettext("user_not_found")}, 404
        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': gettext("user_not_found")}, 404
        user.delete_from_db()
        return {'message': gettext("user_deleted")}, 200


class UserLogin(Resource):

    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = user_schema.load(user_json, partial=('email',))  # no need for email in login if not present

        user = UserModel.find_by_username(user_data.username)

        if user and safe_str_cmp(user.password, user_data.password):
            # Check if user is activated
            confirmation = user.most_recent_confirmation
            if confirmation and confirmation.confirmed:
                access_token = create_access_token(identity=user.id, fresh=True)
                refresh_token = create_refresh_token(user.id)
                return {
                           'access_token': access_token,
                           'refresh_token': refresh_token
                       }, 200
            return {"message": gettext("user_not_confirmed").format(user.username)}, 400

        return {'message': gettext("user_invalid_credentials")}, 401


class UserLogout(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        """Blacklist used token"""
        jti = get_raw_jwt()['jti']  # jti is JWT ID
        BLACKLIST.add(jti)
        return {'message': gettext("user_logged_out")}, 200


class TokenRefresh(Resource):
    @classmethod
    @jwt_refresh_token_required
    def post(cls):
        """Renewing token"""
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200
