"""
*(вместо 1)

Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания.

Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.
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


# Можно улучшить скрипт, проверяя не изменилась ли информация и если изменилась, то пересохранять файл.
# Тогда запись в файл имеет смысл хотя бы в выигрыше скоросте на 2 и последующие разы запуска скрипта.
# В другой раз)
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
            yield line_in_list[0]


def create_dict_of_frequency():
    ip_freq_dict = {}
    for ip in log_list_generator():
        if ip_freq_dict.get(ip) is None:
            ip_freq_dict.update({ip: 1})
        else:
            freq = ip_freq_dict.get(ip) + 1
            ip_freq_dict.update({ip: freq})
    return ip_freq_dict


def get_key(dict, find_value):
    for key, value in dict.items():
        if value == find_value:
            return key


response = get_content(URL)

if response != 0:
    generate_log_file(response)
    ip_freq_dict_1 = create_dict_of_frequency()
    spammer_requests_count = max(ip_freq_dict_1.values())
    spammer = get_key(ip_freq_dict_1, spammer_requests_count)
    print("Наш спамер: ", spammer, "с колличеством запросов ", spammer_requests_count)
else:
    print("Не могу получить данные. Проблемы на стороне сервера.")
