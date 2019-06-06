from models.user import UserModel
from tests.base_test import BaseTest




class UserTest(BaseTest):
    """Access the app context in order to create mock-up db"""
    def test_crud(self):
        with self.app_context():
            user = UserModel('testuser@gmail.com','testuser','abcd')

            self.assertIsNone(UserModel.find_by_username('testuser'), "Found an user with name 'test' before save_to_db")
            self.assertIsNone(UserModel.find_by_id(1), "Found an user with id '1' before save_to_db")

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('testuser'),
                                 "Did not find an user with name 'test' after save_to_db")
            self.assertIsNotNone(UserModel.find_by_id(1), "Did not find an user with id '1' after save_to_db")

            self.assertEqual(user.username, 'testuser',
                             "The name of the user after creation does not equal the constructor argument.")
            self.assertEqual(user.password, 'abcd',
                             "The password of the user after creation does not equal the constructor argument.")


