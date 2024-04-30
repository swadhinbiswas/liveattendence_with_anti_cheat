import bcrypt
class PasswordHash:
    def __init__(self):
        self.salt = bcrypt.gensalt()
    def hash(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.salt)
    def verify(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))