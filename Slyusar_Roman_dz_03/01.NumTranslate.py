"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:

num_translate("one")
"один"

num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую
для перевода: какой тип данных выбрать, в теле функции или снаружи.
"""

NUM_DICT = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}


def num_translate(num):
    """Translation of numbers from English into Russian from a given dictionary"""
    if not isinstance(num, str):
        return 0
    return NUM_DICT.get(num)


print(num_translate("one"))
print(num_translate("eleven"))
print(num_translate(42))
