import bcrypt
from cryptography.fernet import Fernet
import os
class Auth:
    @staticmethod
    def hashing(password):
        password = password.encode()
        return bcrypt.hashpw(password, bcrypt.gensalt()).decode()
    @staticmethod
    def check(user, userName, password):
        if userName == user.getname() and bcrypt.checkpw(password.encode(), user.getpassword().encode()):
            return True

class Encrypt:
    PATH = os.path.dirname(__file__)
    KEY = os.path.join(os.path.dirname(PATH), 'key.txt')
    @classmethod
    def init_loadKey(cls):
        if not os.path.exists(cls.KEY):
            with open(cls.KEY, 'wb') as key_file:
                key = Fernet.generate_key()
                key_file.write(key)
        with open(cls.KEY, 'rb') as key_file:
            key = key_file.read()
        return key
    @classmethod
    def encrypt(cls,data):
        data = data.encode()
        cipher = Fernet(cls.init_loadKey())
        return cipher.encrypt(data).decode()
    @classmethod
    def decrypt(cls,data):
        cipher = Fernet(cls.init_loadKey())
        return cipher.decrypt(data.encode()).decode()

