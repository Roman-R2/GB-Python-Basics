import requests
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
            "rate_date": rate_date,
            "name": currency_dict.get(currency)["Name"]
        }


if __name__ == '__main__':
    rub_to_usd = currency_rates()
    rub_to_eur = currency_rates("EUR")

    print("Курс доллара: \t", rub_to_usd["rate"], rub_to_usd["rate_date"],
          "\nКурс евро: \t\t", rub_to_eur["rate"], rub_to_eur["rate_date"])
    print("\n¯\_(ツ)_/¯")
