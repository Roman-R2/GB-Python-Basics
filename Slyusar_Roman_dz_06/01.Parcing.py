"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида:
(<remote_addr>, <request_type>, <requested_resource>).

Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
"""
import requests

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
LOG_FILE = 'server_logs.txt'


def get_content(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        return 0
    else:
        return resp.content


def generate_log_file(content):
    logs_list = str(content).split("\\n")
    del logs_list[0]
    del logs_list[-1]
    with open(LOG_FILE, 'w+') as f:
        for log in logs_list:
            f.writelines(log + "\n")


def log_list_generator():
    with open(LOG_FILE, 'r') as f:
        for line in f.readlines():
            line_in_list = line.split(" ")
            yield (line_in_list[0], line_in_list[5][1:], line_in_list[6])


response = get_content(URL)

if response != 0:
    generate_log_file(response)
    log_list = list(log_list_generator())
    print(log_list)
else:
    print("Не могу получить данные. Проблемы на стороне сервера.")
