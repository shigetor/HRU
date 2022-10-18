from HRU.User.AbstractUser import AbstractUser


class AdminUser(AbstractUser):
    def __init__(self, login='Admin', password='admin', is_Admin=True):
        super(AdminUser, self).__init__(login, password, is_Admin)

