from flask import session, Response, render_template, redirect, flash, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource
from models.user import UserModel
from flask_login import LoginManager, login_user, logout_user, AnonymousUserMixin, login_required
from schemas.user import UserSchema
from models.confirmation import ConfirmationModel
from libs.strings import gettext

user_schema = UserSchema()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    """Init load active user"""
    return UserModel.find_by_id(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    """Login missing"""
    session['message_warning'] = gettext("user_not_logged_in")
    return redirect(url_for('dashboard'))

class Anonymous(AnonymousUserMixin):
    """Guest user class"""
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
        """Register user and pass to confirmation page"""
        user_data = request.get_json()
        user = user_schema.load(request.get_json())
        if UserModel.find_by_email(user.email):
            return {'message': gettext("user_email_exists"), 'status': 400}

        if "@" not in user.email:
            return {'message': gettext("user_email_incorrect"), 'status': 400}

        if UserModel.find_by_username(user.username):
            return {'message': gettext("user_username_exists"), 'status': 400}

        if user.password != user_data['confirm']:
            return {'message': gettext("user_password_mismatch"), 'status': 400}

        if len(user.password) < 6:
            return {'message': gettext("user_password_too_short"), 'status': 400}

        hashed_password = generate_password_hash(user.password,
                                                 method='sha256')  # password get hashed for security purposes
        new_user = UserModel(email=user.email, username=user.username, password=hashed_password)
        try:
            new_user.save_to_db()
            confirmation = ConfirmationModel(new_user.id)
            confirmation.save_to_db()
            confirmation_id = confirmation.id
            return {'confirmation': confirmation_id, 'status': 200}
        except:
            new_user.delete_from_db()
            return {"message": gettext("user_error_creating"), 'status': 500}
        # return {'user': str(user_data)}

class UserLogin(Resource):

    @classmethod
    def get(cls):
        """Login user view"""
        return Response(render_template('user/login.html'))  # passing login form to login template

    @classmethod
    def post(cls):
        """Login user to application"""
        user_json = request.get_json()
        user_data = user_schema.load(user_json, partial=('username','confirm'))
        user = UserModel.find_by_email(user_data.email)
        if user:
            if check_password_hash(user.password, user_data.password):
                # Check if user is activated
                confirmation = user.most_recent_confirmation
                if confirmation and confirmation.confirmed:
                    session['message_success'] = gettext("user_logged_in").format(user.username)
                    login_user(user, remember=True)
                    return {'status': 200}
                else:
                    return {'message': gettext("user_not_confirmed"), 'status': 401}
            else:
                return {'message': gettext("user_invalid_password"), 'status': 401}
        else:
            return {'message': gettext("user_not_found").format(user_data.email), 'status': 400}


class UserLogout(Resource):
    @classmethod
    @login_required
    def get(cls):
        """logout user"""
        logout_user()
        return redirect("login")



# FOR REST FUNCTIONALITY

class SetPassword(Resource):
    @classmethod
    @login_required
    def post(cls):
        """finds user and changes/set new password. For oauth if user comes back"""
        user_json = request.get_json()
        user_data = user_schema.load(user_json) # username and new password
        user = UserModel.find_by_username(user_data.username)

        if not user:
            return {"message": gettext("user_not_found")}, 400

        user.password = user_data.password
        user.save_to_db()

        return  {"message": gettext("user_password_updated")}, 201

class User(Resource):

    @classmethod
    def get(cls, user_id: int):
        """Find user"""
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': gettext("user_not_found")}, 404
        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        """Delete user"""
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': gettext("user_not_found")}, 404
        user.delete_from_db()
        return {'message': gettext("user_deleted")}, 200
