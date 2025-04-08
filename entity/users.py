class User:
    def __init__(self, user_id=0, username="", password="", email=""):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__email = email

    @property
    def user_id(self):
        return self.__user_id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @username.setter
    def username(self, username):
        self.__username = username

    @password.setter
    def password(self, password):
        self.__password = password

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return f"User [ID: {self.__user_id}, Username: {self.__username}, Email: {self.__email}]"
