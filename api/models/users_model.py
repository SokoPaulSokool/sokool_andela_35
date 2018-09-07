
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class UserList:
    def __init__(self):
        self.users_list = []
