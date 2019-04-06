from tests.base_test import BaseTest
from app import mongo



class AlgorithmTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            test_algorithm = {"algorithm": "test", "description": "testing"}
            tests = mongo.db.tests
            self.assertEqual(mongo.db.tests.find({"algorithm": "test"}).count(), 0,
                             "Found an Algorithhm in mongo database, but expected not to")

            tests.insert_one(test_algorithm)

            self.assertIsNotNone(mongo.db.tests.find({"algorithm": "test"}),
                             "Algorithm was not saved to mongodb")

            mongo.db.tests.remove({"algorithm": "test"})

            self.assertEqual(mongo.db.tests.find({"algorithm": "test"}).count(), 0,
                             "Found an Algorithhm in mongo database, but expected not to")


