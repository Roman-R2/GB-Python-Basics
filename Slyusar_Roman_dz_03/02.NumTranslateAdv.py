"""
2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:

num_translate_adv("One")
"Один"

num_translate_adv("two")
"два"
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
    if num.istitle():
        return NUM_DICT.get(num.lower()).title()
    else:
        return NUM_DICT.get(num)


print(num_translate("One"))
print(num_translate("seven"))
print(num_translate("eleven"))
print(num_translate(42))
