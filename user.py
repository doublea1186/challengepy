class User:

    def __init__(self, name, user, password, likes):
        self.name = name
        self.user = user
        self.password = password
        self.likes = likes

    def set_name(self, name):
        self.name = name

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    def set_likes(self, likes):
        self.likes = likes

    def get_name(self):
        return self.name

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_likes(self):
        return self.likes
