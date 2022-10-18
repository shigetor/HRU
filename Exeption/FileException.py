from HRU.Exeption.BaseException import BasicException


class FileException(BasicException):
    def __init__(self, file_name):
        self.file_name = file_name
        super(FileException, self).__init__(f'Файла {file_name} не существует')
