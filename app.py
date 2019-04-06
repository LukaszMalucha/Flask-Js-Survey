import os
# import env

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from flask_restful import Api

from resources.user import UserRegister, UserLogin, UserLogout, login_manager

# Settings
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# For User Credentials:
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# For Suggested Questions:
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = False
api = Api(app)

Bootstrap(app)
login_manager.init_app(app)
mongo = PyMongo(app)

# Register Resources
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

# Dashboard Blueprint
from project.dashboard.views import dashboard_blueprint
app.register_blueprint(dashboard_blueprint)


# Error Handlers
@app.errorhandler(404)
def error404(error):
    return render_template('404.html')


@app.errorhandler(500)
def error500(error):
    return render_template('500.html')


## APP INITIATION

if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    # app.run(debug=True)

# Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)