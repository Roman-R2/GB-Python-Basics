"""
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если,
например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).

Создать новый список, содержащий те же цены, но отсортированные по убыванию.

Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

"""

price_list = [57.8, 46.51, 97, 4.3, 10, 23.7, 45.09, 99.99, 43, 55]


def digitfilter(price):
    if isinstance(price, float):
        penny = str(price).split(".")[-1]
        if len(str(penny)) == 1:
            penny = penny + "0"
        str_list = ' '.join([str(int(price)), "руб", penny, "коп"])
        return str_list
    elif isinstance(price, int):
        str_list = ' '.join([str(price), "руб", "00", "коп"])
        return str_list
    else:
        return 0


def print_price_list(list):
    for price in list:
        print(digitfilter(price))


print("Просто выводим список:")
print_price_list(price_list)

print("Сортитуем список:")
price_list.sort()
print_price_list(price_list)

print("Новый список, отсортированный по убыванию:")
new_price_list = price_list.copy()
print("Проверим, что это разные объекты:", id(price_list), id(new_price_list))
new_price_list.sort(reverse=True)
print_price_list(new_price_list)

print("Пять самых дорогих товаров:")
print_price_list(new_price_list[:5])
