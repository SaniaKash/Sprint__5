import random


class UserLogin:

    @staticmethod
    def password_false():
        password_false = random.randrange(100, 999)
        return password_false

    @staticmethod
    def password():
        password = random.randrange(100000, 999999)
        return password

    @staticmethod
    def login():
        login = f'alekskashtanov{random.randrange(100000, 999000)}@gmail.com'
        return login
