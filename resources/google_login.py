from flask import g, request, url_for, redirect
from flask_login import login_user
from flask_restful import Resource

from models.user import UserModel
from oa import google


class GoogleLogin(Resource):
    @classmethod
    def get(cls):
        """send user to authorization page"""
        return google.authorize(url_for("google.authorize", _external=True))  # external because we build full url
    
    
class GoogleAuthorize(Resource):
    @classmethod
    def get(cls):
        """Take google data and send it to google post request to retrieve user access token"""
        resp = google.authorized_response()

        if resp is None or resp.get('access_token') is None:
            error_response = {
                "error": request.args['error'],
                "error_description": request.args["error_description"]
            }
            return error_response

        g.access_token = resp['access_token']  # put access token inside flask_global
        google_user = google.get('user')
        google_email = google_user.data['login'] ??????????????????????????????????????????????

        user = UserModel.find_by_username(google_email)

        if not user:
            user = UserModel(username=google_email, email=google_email,
                             password=None)  # if login with google, there is no password given
            user.save_to_db()

        login_user(user)
        return redirect('/')
