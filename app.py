import os

from marshmallow import ValidationError

import env

from flask import Flask, render_template, jsonify, session
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, UserLogin, UserLogout, login_manager
from resources.confirmation import ConfirmationPage, Confirm
from blacklist import BLACKLIST
from ma import ma

# Settings
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# For User Credentials:
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['JWT_SECRET_KEY'] = os.environ["JWT_SECRET_KEY"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True
# For Suggested Questions:
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

api = Api(app)

Bootstrap(app)
mongo = PyMongo(app)

# Init login manager
login_manager.init_app(app)

# Enable jwt authentication (check resources.user.UserLogin)
jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def chcek_if_token_in_blacklist(decrypted_token):
    return decrypted_token['identity'] in BLACKLIST

# Register Resources
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(ConfirmationPage, '/user_confirmation/<string:confirmation_id>')
api.add_resource(Confirm, '/confirm')


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    """Main dashboard"""
    message_success = session.get('message_success', None)  # Success login message
    session['message_success'] = None
    return render_template('dashboard.html', message_success=message_success)


# SciKit Map:
@app.route('/map')
def map():
    return render_template('map.html')


# Error Handlers
@app.errorhandler(404)
def error404(error):
    return render_template('404.html')


@app.errorhandler(500)
def error500(error):
    return render_template('500.html')


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(error):
    return jsonify(error.messages), 400


## APP INITIATION

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    ma.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run()

# Heroku
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
