"""
*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield
"""


def nums_generator(n):
    return (num for num in range(1, n + 1, 2))


number = nums_generator(15)

print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
