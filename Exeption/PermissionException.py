from HRU.Exeption.BaseException import BasicException


class PermissionException(BasicException):
    def __init__(self, user):
        self.user = user
        super(PermissionException, self).__init__(f'У пользователя {user} нет данных прав')


class NotExistUserException(BasicException):
    def __init__(self, flag, login):
        self.flag = flag
        self.login = login
        super(NotExistUserException, self).__init__(f'{login} не существует, попробуйте еще раз')


class ExistUserException(BasicException):
    def __init__(self, login):
        self.login = login
        super(ExistUserException, self).__init__(f'Пользователь с логином {login} существует, создайте нового '
                                                 f'пользователя')


