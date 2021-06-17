"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя
пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError.

Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}

email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re


def email_parse(some_string):
    if not isinstance(some_string, str):
        error_message = "wrong type: {}".format(type(some_string))
        raise TypeError(error_message)
    RE_EMAIL = re.compile(r'^[a-zA-Z0-9]{1,100}[@][a-z]{2,30}\.[a-z]{2,4}')
    if not RE_EMAIL.findall(some_string):
        error_message = "wrong email:  {}".format(some_string)
        raise ValueError(error_message)
    else:
        # Эта строка чисто по приколу - вместо регулярного выражения :)
        return {'username': some_string.split("@")[0], 'domain': some_string.split("@")[1].split(".")[0]}


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
