from re import match


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


class UserList:
    def __init__(self):
        self.users_list = []
