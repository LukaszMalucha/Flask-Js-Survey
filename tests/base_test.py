from unittest import TestCase
from app import app
from db import db
from app import mongo

"""
Parent Class for each non-unit test. Creates new, blank mock-up database and tears it down once finished.
"""

class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """ Set up new database """
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'
        # init app context
        with app.app_context():
            db.init_app(app)


    def setUp(self):
        with app.app_context():
            db.create_all()

        # get test client
        self.app = app.test_client
        self.app_context = app.app_context


    def tearDown(self):
        """ Destroy test db"""
        with app.app_context():
            db.session.remove()
            db.drop_all()
            mongo.db.drop_collection("tests")