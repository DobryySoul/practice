import re


class Registration:

    def __init__(self, login, password):
        self.my_login = login
        self.my_password = password

    @property
    def my_login(self):
        return self.__login

    @property
    def my_password(self):
        return self.__password

    @my_login.setter
    def my_login(self, pas_login):
        if pas_login.count("@") != 1:
            raise ValueError('Login must include at least one "@"')
        elif pas_login.count('.') != 1:
            raise ValueError('Login must include at least one "."')
        else:
            self.__login = pas_login

    @my_password.setter
    def my_password(self, pas_password):
        if not isinstance(pas_password, str):
            raise TypeError('Пароль должен быть строкой')
        elif not 4 <= len(pas_password) and len(pas_password) >= 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12')
        elif not (re.search('[0-9]', pas_password)):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif not (re.search('[a-z]', pas_password) and re.search('[A-Z]', pas_password)):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        elif not (re.search('[a-z]', pas_password) or re.search('[A-Z]', pas_password)):
            raise ValueError('Пароль должен содержать только латинские алфавит')
        else:
            self.__password = pas_password

    @staticmethod
    def check_password_dictionary():
        with open('easy_passwords.txt', 'r') as text_file:
            for string in text_file.readlines():
                if string != Registration.my_password:
                    raise ValueError('Ваш пароль содержится в списке самых легких ')


acc1 = Registration('Niktia@.@mailru', '1231ASDdd')
#acc1.my_login = 'Niktia@@.mailru'
print(acc1.my_login)
print(acc1.my_password)
print(acc1.check_password_dictionary())