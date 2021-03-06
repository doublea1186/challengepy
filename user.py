import pickle


class User:
    def __init__(self, name, user, password, likes):
        self.name = name
        self.user = user
        self.password = password
        self.likes = likes

    def save_user(self):
        user_info = self.read_user_data()
        for x in user_info:
            if self.user == x.user:
                return False

        user_info.append(self)
        with open('user.info', 'wb') as config_file:
            pickle.dump(user_info, config_file)
        return True

    def find_user_index(self):
        user_info = self.read_user_data()
        for x in user_info:
            if x.user == self.user:
                return user_info.indexOf(x)

        return -1

    def authenticate(self):
        user_info = self.read_user_data()
        for x in user_info:
            if (x.user == self.user) & (x.password == self.password):
                return True
        return False

    @staticmethod
    def init_users():
        users = []
        users.append(User('admin', 'admin', 'password', ""))
        with open('user.info', 'wb') as config_file:
            pickle.dump(users, config_file)

    @staticmethod
    def contains(list, filter):
        for x in list:
            if filter(x):
                return True
        return False

    @staticmethod
    def read_user_data():
        with open('user.info', 'rb') as config_file:
            return pickle.load(config_file)

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
