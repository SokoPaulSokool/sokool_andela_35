from re import match
from flask import json


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def is_validName(self):
        if self.username.isalpha():
            return True
        return False

    def is_validEmail(self):
        if bool(
            match(
                r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",
                self.email)):
            return True
        return False

    def is_valid_user(self):
        if self.is_validEmail() and self.is_validName():
            return True
        return False

    def toJSON(self):
        # return json.dumps(self, default=lambda o: o.__dict__)
        return {"username": self.username, "email": self.email, "password": self.password}


class UserList:
    def __init__(self):
        self.list = {}

    def get_all_users(self):
        all_users = []
        for the_key, value in self.list.items():
            all_users.append(value.toJSON())
        return all_users

    def add_user(self, user: User):
        if user.is_valid_user():
            if (self.user_exists(user.email)):
                return "User already exists"
            self.list[user.email] = user
            return "success"
        else:
            return "invalid user"

    def user_exists(self, email):
        return self.list.__contains__(email)

    def get_user_by_email(self, email):
        if (self.user_exists(email)):
            return self.list[email]
        return "User does not exist"

    def delete_user(self, email):
        if (self.user_exists(email)):
            self.list.pop(email)
            return "deleted"
        else:
            return "User does not exist"
