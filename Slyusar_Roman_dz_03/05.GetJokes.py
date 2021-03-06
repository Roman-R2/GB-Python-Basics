"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:

get_jokes(2)
    ["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

"""
import random


def get_jokes(quantity=1):
    """Function that returns jokes from random words"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if not isinstance(quantity, int):
        return 0

    jokes_list = []

    while quantity:
        jokes_list.append(
            random.choice(nouns) + " " + random.choice(adverbs) + " " + random.choice(adjectives))
        quantity -= 1

    return jokes_list


print(get_jokes())
