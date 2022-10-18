import json
import os
from HRU.Exeption.PermissionException import *
from HRU.User.User import User
import hashlib


def check_read_object(name_file, login):
    with open('file_perm.json') as json_file:
        flag = False
        data = json.load(json_file)
        size_json = len(data['files'])
        for j in range(0, size_json):
            for item in data['files'][j]:
                if item == name_file:
                    var = j
        for i in range(0, (len(data['files'][var][f'{name_file}']))):
            if (data['files'][var][f'{name_file}'][i]['user'] == login) and \
                    (data['files'][var][f'{name_file}'][i]['read'] == '1' or
                     data['files'][var][f'{name_file}'][i]['owner'] == '1'):
                flag = True
        return flag


def check_write_object(name_file, login):
    with open('file_perm.json') as json_file:
        flag = False
        data = json.load(json_file)

        size_json = len(data['files'])
        for j in range(0, size_json):
            for item in data['files'][j]:
                if item == name_file:
                    var = j
        for i in range(0, (len(data['files'][var][f'{name_file}']))):
            if (data['files'][var][f'{name_file}'][i]['user'] == login) and \
                    (data['files'][var][f'{name_file}'][i]['write'] == '1' or
                     data['files'][var][f'{name_file}'][i]['owner'] == '1'):
                flag = True
        return flag


def check_owner_object(name_file, login):
    with open('file_perm.json') as json_file:
        flag = False
        data = json.load(json_file)
        size_json = len(data['files'])
        var = 0
        for j in range(0, size_json):
            for item in data['files'][j]:
                if item == name_file:
                    var = j
        for i in range(0, (len(data['files'][var][f'{name_file}']))):
            if data['files'][var][f'{name_file}'][i]['user'] == login \
                    and data['files'][var][f'{name_file}'][i]['owner'] == '1':
                flag = True
        return flag


def create_file_system():
    data = {'files': []}
    with open('file_perm.json', 'w') as outfile:
        json.dump(data, outfile)


def init():
    a = User()
    data = {'users': []}
    key = hashlib.pbkdf2_hmac('sha256', a.get_password().encode('utf-8'), salt, 100000)
    data['users'].append({
        'login': f'{a.get_login()}',
        'password': f'{key}',
        'is_admin': f'{a.get_is_admin()}'
    })

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    create_file_system()


salt = b'\xdd0\x0b\xe0?\x97IKBo\xf7\x94\x07\n\x0b\xdc\xb5\x06SN\xb3[\x1f\xd3\xbc;\xa4\xd6\x0c\xb2$\xd6'


def create_user(login, password, is_admin=False):
    user = User(f'{login}', f'{password}', is_admin)
    flag = True

    with open('data.json') as json_file:
        data1 = json.load(json_file)
        for item in data1['users']:
            if item['login'] == user.get_login():
                flag = False

    if not flag:
        print('Такой юзер уже есть')
    else:
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        data1['users'].append({
            'login': f'{user.get_login()}',
            'password': f'{key}',
            'is_admin': f'{user.get_is_admin()}',
            'salt': f'{salt}',
        })
        with open('data.json', 'w') as json_file:
            json.dump(data1, json_file)


def check_permission():
    flag = False
    print('Введите логин и пароль')
    login = input('Логин: ')
    password = input('Пароль: ')
    with open('data.json') as json_file:
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        data1 = json.load(json_file)
        for item in data1['users']:
            if item['login'] == login and item['password'] == str(key):
                flag = True
    if flag:
        print('Все верно')
        return flag, login
    else:
        raise NotExistUserException(flag, login)


def create_object(name_object, content=''):
    permission, login = check_permission()

    if permission:
        new_file = open(f'{name_object}', 'w+')
        new_file.write(f'{content}')
        new_file.close()

        with open('file_perm.json') as json_file:
            data1 = json.load(json_file)
        data1['files'].append({f'{name_object}': [{
            'user': f'{login}',
            'read': f'1',
            'write': f'1',
            'owner': f'1',
        }]})

        with open('file_perm.json', 'w') as json_file:
            json.dump(data1, json_file)


def read_object(name_file):
    permission, login = check_permission()
    if permission:
        ch = check_read_object(name_file, login)
        if ch:
            file = open(f'{name_file}', 'r')
            print(file.readline())
            file.close()
        else:
            raise PermissionException(login)


def write_in_object(name_file, content):
    permission, login = check_permission()
    if permission:
        ch = check_write_object(name_file, login)
        if ch:
            file = open(f'{name_file}', 'a')
            file.write(content)
            file.close()
        else:
            raise PermissionException(login)


def delete_subject(name_object):
    is_admin = 'False'
    permission, login = check_permission()
    if permission:
        with open('data.json', 'r') as fp:
            data = json.load(fp)
        for item in data['users']:
            if item['login'] == login:
                is_admin = item['is_admin']
        size_data = len(data['users'])
        if is_admin == 'True':
            for i in range(0, size_data):
                if data['users'][i]['login'] == name_object:
                    print(True)
                    del data['users'][i]
                    break
        else:
            raise PermissionException(login)
        with open('data.json', 'w') as fp1:
            json.dump(data, fp1)


def delete_object(name_subject):
    is_admin = 'False'
    permission, login = check_permission()
    if permission:
        ch = check_owner_object(name_subject, login)
        with open('data.json', 'r') as fp:
            data = json.load(fp)
        with open('file_perm.json', 'r') as fp1:
            data1 = json.load(fp1)
        for item in data['users']:
            if item['login'] == login:
                is_admin = item['is_admin']
        if is_admin == 'True' or ch is True:
            if os.path.isfile(f'{name_subject}'):
                os.remove(f'{name_subject}')
            size_json = len(data1['files'])
            for j in range(0, size_json):
                print(j)
                for item in data1['files'][j]:

                    if item == f'{name_subject}':
                        del data1['files'][j]
            print(f'Файл {name_subject} был удален {login}')
        else:
            raise PermissionException(login)
        with open('file_perm.json', 'w') as fp:
            json.dump(data1, fp)


def give_access_to_user(name_object, name_subject, access):
    permission, login = check_permission()
    r = '0'
    w = '0'
    o = '0'
    if access.find("r") != -1:
        r = 1
    if access.find("w") != -1:
        w = 1
    if access.find("o") != -1:
        o = 1
        r = 1
        w = 1

    if permission:
        ch = check_owner_object(name_subject, login)
        if ch is True:
            with open('file_perm.json') as fp:
                data = json.load(fp)
                size_json = len(data['files'])
                for j in range(0, size_json):
                    for item in data['files'][j]:
                        if item == f'{name_subject}':
                            data['files'][j][f'{name_subject}'].append({
                                'user': f'{name_object}',
                                'read': f'{r}',
                                'write': f'{w}',
                                'owner': f'{o}',
                            })
                with open('file_perm.json', 'w') as json_file:
                    json.dump(data, json_file)
