class SignUp():

    def __init__(self):
        """initialize user bio dictionary"""
        self.user_bio = dict()

    def add(self, username, email, password):
        """add user to user_bio with username as key"""
        self.user_bio[username] = {password:password, email:email}

    