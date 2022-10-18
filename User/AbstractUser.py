from abc import ABC, abstractmethod


class AbstractUser(ABC):
    def __init__(self, login, password, is_admin):
        self._login = login
        self._password = password
        self._is_admin = is_admin

    def get_login(self):
        return self._login

    def set_login(self, login):
        self._login = login

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def get_is_admin(self):
        return self._is_admin

    def set_is_admin(self, is_admin):
        self._is_admin = is_admin

