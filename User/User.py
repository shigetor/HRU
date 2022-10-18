from HRU.User.AbstractUser import AbstractUser


class User(AbstractUser):
    def __init__(self, login='User', password='1234', is_admin=False):
        super(User, self).__init__(login, password, is_admin)


