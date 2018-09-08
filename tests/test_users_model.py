import unittest
from api.models.users_model import User, GuestList


class TestUser(unittest.TestCase):
    def setUp(self):
        self.list_of_users = GuestList()
        self.user = User('soko', 'sopapaso73@gmail.com', '4321')

    def teardown(self):
        del self.list_of_users
        del self.user

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)

    def test_valid_user_inputs(self):
        self.assertEqual(self.user.is_valid_user(), True)

    def test_invalid_email(self):
        invalid_email_user = User('soko', 'paul', '4321')
        self.assertEqual(invalid_email_user.is_validEmail(), False)
        self.assertEqual(invalid_email_user.is_valid_user(), False)

    def test_invalid_name(self):
        invalid_name_user = User('soko@paul', 'paul', '4321')
        self.assertEqual(invalid_name_user.is_validName(), False)
        self.assertEqual(invalid_name_user.is_valid_user(), False)

    def test_adding_validuser_to_list(self):
        self.assertEqual(self.list_of_users.add_user(self.user), 'success')
        self.assertEqual(len(self.list_of_users.list), 1)

    def test_adding_invalid_validuser_to_list(self):
        invalid_email_user = User('soko', 'paul', '4321')
        self.assertEqual(self.list_of_users.add_user(
            invalid_email_user), 'invalid user')

    def test_adding_duplicate_validuser_to_list(self):
        self.assertEqual(self.list_of_users.add_user(self.user), 'success')
        self.assertEqual(self.list_of_users.add_user(
            self.user), 'User already exists')
        self.assertEqual(len(self.list_of_users.list), 1)

    def test_getting_user(self):
        self.list_of_users.add_user(self.user)
        self.assertEqual(self.list_of_users.get_user_by_email(
            self.user.email), self.user)

    def test_getting_user_who_doesnot_exist(self):
        new_user = User('soko', 'paul@gmail.com', '4321')
        self.assertEqual(self.list_of_users.get_user_by_email(
            new_user.email), 'User does not exist')

    def test_deleting_user(self):
        self.list_of_users.add_user(self.user)
        self.assertEqual(self.list_of_users.delete_user(
            self.user.email), "deleted")
        self.assertEqual(len(self.list_of_users.list), 0)

    def test_deleting_user_who_doesnot_exist(self):
        new_user = User('soko', 'paul@gmail.com', '4321')
        self.list_of_users.add_user(self.user)
        self.assertEqual(len(self.list_of_users.list), 1)
        self.assertEqual(self.list_of_users.delete_user(
            new_user.email), 'User does not exist')
        self.assertEqual(len(self.list_of_users.list), 1)
