from flask import session, Response, render_template, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource
from models.user import UserModel
from libs.forms import RegisterForm, LoginForm
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
        form = RegisterForm()
        users = UserModel.find_by_id(1)
        conf = ConfirmationModel.query.all()
        #  passing signup form to signup template
        return Response(render_template('user/register.html', form=form, users=users, conf=conf))

    @classmethod
    def post(cls):
        form = RegisterForm()
        if form.validate_on_submit():
            if UserModel.find_by_email(form.email.data):
                return {'message': gettext("user_username_exists"), 'alert': 'alert alert-danger'}, 400

            if UserModel.find_by_username(form.username.data):
                return {'message': gettext("user_email_exists"), 'alert': 'alert alert-danger'}, 400

            hashed_password = generate_password_hash(form.password.data,
                                                     method='sha256')  ## password get hashed for security purposes
            new_user = UserModel(email=form.email.data, username=form.username.data, password=hashed_password)
            try:
                new_user.save_to_db()
                confirmation = ConfirmationModel(new_user.id)
                confirmation.save_to_db()
                # new_user.send_confirmation_email()
                # login_user(new_user)
                conf = str(confirmation.id)
                # return Response(render_template('user/confirmation_page.html', email='asd'))
                return redirect(url_for("confirmationemail", confirmation_id = conf))
            except:
                new_user.delete_from_db()
                return {"message": gettext("user_error_creating")}, 500

        return Response(render_template('user/register.html', form=form))  # passing signup form to signup template


class UserLogin(Resource):

    @classmethod
    def get(cls):
        form = LoginForm()

        # alert alert-success
        return Response(render_template('user/login.html', form=form))  ## passing login form to login template

    @classmethod
    def post(cls):
        form = LoginForm()

        if form.validate_on_submit():  ## if form was submitted....
            user = UserModel.find_by_email(email=form.email.data)
            if user:
                if check_password_hash(user.password, form.password.data):
                    session['current_user'] = user.email
                    flash(f'You have successfully logged in as {user.email}', 'alert alert-success')
                    login_user(user)
                    return redirect("/")
            else:
                flash(u'Invalid Email or Password provided', 'alert alert-danger')

        return Response(render_template('user/login.html', form=form))


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
