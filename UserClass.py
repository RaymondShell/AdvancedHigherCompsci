from datetime import datetime
class User:
    def __init__(self, username, password):
        self._id = username
        self.__password = password
        self.__signUpDate = datetime.now()
        self.__admin = False
    def get_username(self):
        return self._id
    def get_password(self):
        return self.__password
    def get_signUpDate(self):
        return self.__signUpDate
    def get_admin(self):
        return self.__admin
    def set_admin(self, value):
        self.__admin = value