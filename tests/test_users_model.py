import unittest
from api.models.users_model import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('soko', 'sopapaso73@gmail.com', '4321')

    def teardown(self):
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
