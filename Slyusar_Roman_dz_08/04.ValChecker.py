"""
 Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""


def val_checker(func):
    def _val_checker(for_func):
        def wrapper(x):
            if not func(x):
                msg = "wrong val {}".format(x)
                raise ValueError(msg)
            return for_func(x)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
