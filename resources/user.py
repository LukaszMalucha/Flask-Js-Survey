from flask import session, Response, render_template, redirect, flash, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource
from models.user import UserModel
from libs.forms import LoginForm
from flask_login import LoginManager, login_user, logout_user, AnonymousUserMixin
from schemas.user import UserSchema
from models.confirmation import ConfirmationModel
from libs.strings import gettext

user_schema = UserSchema()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return UserModel.find_by_id(int(user_id))


class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.email = 'Guest'


login_manager.anonymous_user = Anonymous


class UserRegister(Resource):

    @classmethod
    def get(cls):
        """Register User function"""
        return Response(render_template('user/register.html'))

    @classmethod
    def post(cls):
        user_data = request.get_json()
        if UserModel.find_by_email(user_data['email']):
            return {'message': gettext("user_email_exists"), 'status': 400}

        if "@" not in user_data['email']:
            return {'message': gettext("user_email_incorrect"), 'status': 400}

        if UserModel.find_by_username(user_data['username']):
            return {'message': gettext("user_username_exists"), 'status': 400}

        if user_data['password'] != user_data['confirm']:
            return {'message': gettext("user_password_mismatch"), 'status': 400}

        if len(user_data['password']) < 6:
            return {'message': gettext("user_password_too_short"), 'status': 400}

        hashed_password = generate_password_hash(user_data['password'],
                                                 method='sha256')  # password get hashed for security purposes
        new_user = UserModel(email=user_data['email'], username=user_data['username'], password=hashed_password)
        try:
            new_user.save_to_db()
            confirmation = ConfirmationModel(new_user.id)
            confirmation.save_to_db()
            confirmation_id = confirmation.id
            return {'confirmation': confirmation_id, 'status': 200}
        except:
            new_user.delete_from_db()
            return {"message": gettext("user_error_creating"), 'status': 500}


class UserLogin(Resource):

    @classmethod
    def get(cls):
        """Login user function"""
        return Response(render_template('user/login.html'))  # passing login form to login template

    @classmethod
    def post(cls):
        user_data = request.get_json()

        user = UserModel.find_by_email(user_data['email'])
        if user:
            if check_password_hash(user.password, user_data['password']):
                session['message_success'] = gettext("user_logged_in").format(user.username)
                login_user(user)
                return {'status': 200}
            else:
                return {'message': gettext("user_invalid_password"), 'status': 400}
        else:
            return {'message': gettext("user_not_found").format(user_data['email']), 'status': 400}


class UserLogout(Resource):

    @classmethod
    def get(cls):
        logout_user()
        return redirect("login")


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
