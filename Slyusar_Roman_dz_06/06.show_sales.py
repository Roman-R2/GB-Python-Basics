"""
Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два
скрипта с интерфейсом командной строки: для записи данных и для вывода на экран
записанных данных.

При записи передавать из командной строки значение суммы продаж.

Для чтения данных реализовать в командной строке следующую логику:
    ● просто запуск скрипта — выводить все записи;
    ● запуск скрипта с одним параметром-числом — выводить все записи с номера, равного
    этому числу, до конца;
    ● запуск скрипта с двумя числами — выводить записи, начиная с номера, равного
    первому числу, по номер, равный второму числу, включительно.

Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.

Примеры запуска скриптов:
python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
"""

import argparse

SALE_DB = "bakers_sale_db.txt"


def show_all_sales():
    with open(SALE_DB, "r") as f:
        for line in f.readlines():
            yield line.replace("\n", "")


def show_sales_from_position(position):
    count = 2
    with open(SALE_DB, "r") as f:
        for line in f.readlines():
            if count > position:
                yield line.replace("\n", "")
            count += 1


def show_sales_slice(from_line, to_line):
    count = 2
    with open(SALE_DB, "r") as f:
        for line in f.readlines():
            if from_line < count < to_line + 2:
                yield "строка " + str(count - 1) + ": " + line.replace("\n", "")
            count += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Запись продажи булошной")
    parser.add_argument(
        '--start',
        type=int,
        default=0,
        help='Start position (default: 0)'
    )
    parser.add_argument(
        '--end',
        type=int,
        default=0,
        help='End position (default=0, to end)'
    )

    show_sale = parser.parse_args()

    start_position = show_sale.start
    end_position = show_sale.end

    if not start_position and not end_position:
        for item in show_all_sales():
            print(item)
    elif start_position and not end_position:
        for item in show_sales_from_position(start_position):
            print(item)
    elif start_position and end_position:
        for item in show_sales_slice(start_position, end_position):
            print(item)
    else:
        print("Эта часть программы не должна была выполнится. Ааааа паника!")
