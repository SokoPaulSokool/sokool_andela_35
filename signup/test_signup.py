import unittest
from signup import SignUp


class SignUpTest(unittest.TestCase):

    def setUp(self):
        """set up signup"""
        self.signup = SignUp()

    def test_add_user(self):
        """test adding user"""
        self.signup.add("John Doe", "sopapaso73@gmail.com", "12345")
        self.assertEqual(len(self.signup.user_bio), 1)

    def test_missing_arguments(self):
        with self.assertRaises(TypeError):
            self.signup.add('John')
            self.signup.add('John', "soko@gmail.com")
            self.signup.add("John Doe", "sopapaso73@gmail.com", "12345")
