"""
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
"""

import utils

rub_to_eur = utils.currency_rates("BRL")

print(rub_to_eur["name"], " стоит ", rub_to_eur["rate"], " рублей на дату", rub_to_eur["rate_date"])