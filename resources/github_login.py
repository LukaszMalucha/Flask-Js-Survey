from flask import g, request, url_for, redirect, session
from flask_login import login_user
from flask_restful import Resource

from models.user import UserModel
from oa import github


class GithubLogin(Resource):
    @classmethod
    def get(cls):
        """send user to authorization page"""
        return github.authorize(url_for("github.authorize", _external=True))  # external beacuse we build full url


class GithubAuthorize(Resource):
    @classmethod
    def get(cls):
        """Take github data and send it to GitHub post request to retrieve user access token"""
        resp = github.authorized_response()

        if resp is None or resp.get('access_token') is None:
            error_response = {
                "error": request.args['error'],
                "error_description": request.args["error_description"]
            }
            return error_response ########## URL DO TEGO I GOOGLE

        g.access_token = resp['access_token']  # put access token inside flask_global
        github_user = github.get('user')
        github_email = github_user.data['login']
        user = UserModel.find_by_username(github_email)

        if not user:
            user = UserModel(username=github_email, email=github_email,
                             password=None)  # if login with github, there is no password given
            user.save_to_db()

        login_user(user)

        return redirect('/')  ## URL FOR
