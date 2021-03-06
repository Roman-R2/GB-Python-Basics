"""
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки.
Сформировать из этих имён и вывести на экран фразы вида:
'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
Можно ли при этом не создавать новый список?

"""

employers_list = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАй',
    'директор аэлита'
]


def namefilter(str):
    return str.title()


for element in employers_list:
    employer_name = element.split()[-1]
    print('Привет, ', namefilter(employer_name))
