"""
*(вместо 4)
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:

> python task_4_5.py USD
75.18, 2020-09-05

"""

import requests
import argparse
from bs4 import BeautifulSoup
from datetime import datetime


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

    currency_date = soup.find("valcurs")["date"]
    rate_date = datetime.strptime(currency_date, '%d.%m.%Y').date()

    currency_dict = get_currency_dict(valute)

    if currency_dict.get(currency) is None:
        return None
    else:
        return {
            "rate": currency_dict.get(currency)["Value"],
            "rate_date": rate_date
        }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Return the rate of currency")
    parser.add_argument('--cur', type=str)

    currency = parser.parse_args()
    currency_dict = currency_rates(currency.cur)

    if currency_dict is None:
        print("Воспользуйтесь консолью!")
    else:
        print(currency_dict["rate"], currency_dict["rate_date"])
