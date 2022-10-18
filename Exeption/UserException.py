from HRU.Exeption.BaseException import BasicException


class UserException(BasicException):
    def __init__(self, user_name):
        self.user_name = user_name
        super(UserException, self).__init__(f'Пользователя {user_name} не существует')

