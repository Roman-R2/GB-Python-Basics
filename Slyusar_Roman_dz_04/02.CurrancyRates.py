"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.

В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float.

Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
"""
import requests
from bs4 import BeautifulSoup


def get_currency_dict(valute):
    currency_dict = {}
    for item in valute:
        currency_name = item.find("charcode").text
        currency_dict.update({currency_name: {
            "NumCode": item.find("numcode").text,
            'CharCode': item.find("charcode").text,
            "Nominal": item.find("nominal").text,
            "Name": item.find("name").text,
            "Value": item.find("value").text
        }})
    return currency_dict


def currency_rates(currency="USD"):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.status_code != 200:
        return 0

    soup = BeautifulSoup(response.content, 'lxml')
    valute = soup.find_all("valute")

    currency_dict = get_currency_dict(valute)

    if currency_dict.get(currency) is None:
        return None
    else:
        return currency_dict.get(currency)["Value"]


rub_to_usd = currency_rates()
rub_to_eur = currency_rates("EUR")

print("Курс доллара: \t", rub_to_usd, "\nКурс евро: \t\t", rub_to_eur)
print("\n¯\_(ツ)_/¯")
