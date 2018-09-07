import unittest
from api.models.users_model import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('soko', 'sopapaso73@gmail.com', '4321')

    def teardown(self):
        del self.user

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)
