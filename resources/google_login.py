from flask import g, request, url_for, redirect
from flask_login import login_user
from flask_restful import Resource

from models.user import UserModel
from oa import github