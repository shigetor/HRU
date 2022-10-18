from HRU.Controller.init_system import *
from HRU.Exeption import UserException, FileException
from HRU.Exeption.PermissionException import NotExistUserException, PermissionException

try:
    give_access_to_user('Pasha','test.txt','r')
except PermissionException as e:
    print(e)
except ExistUserException as f:
    print(f)
except FileException as r:
    print(r)
except UserException as u:
    print(u)
except NotExistUserException as n:
    print(n)
