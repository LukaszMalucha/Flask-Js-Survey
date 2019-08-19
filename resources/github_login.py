from flask import g, request, url_for
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource

from models.user import UserModel
from oa import github