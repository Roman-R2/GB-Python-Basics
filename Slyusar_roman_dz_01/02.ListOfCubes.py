"""
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!
"""

list_of_cubes = []

for i in range(1, 1000, 2):
    list_of_cubes.append(i ** 3)

print("Список, состоящий из кубов нечётных чисел от 0 до 1000: ", list_of_cubes)

# можно было реализовать с помошью функции и какой-нибудь рекурсии, но мы пока о них не знаем в этом курсе :)
sum_of_digits_div_by_seven = 0
for element in list_of_cubes:
    temp_sum = 0
    temp_sum += element // 1000000000
    temp_sum += (element % 1000000000) // 100000000
    temp_sum += (element % 100000000) // 10000000
    temp_sum += (element % 10000000) // 1000000
    temp_sum += (element % 1000000) // 100000
    temp_sum += (element % 100000) // 10000
    temp_sum += (element % 10000) // 1000
    temp_sum += (element % 1000) // 100
    temp_sum += (element % 100) // 10
    temp_sum += element % 10
    if temp_sum % 7 == 0:
        sum_of_digits_div_by_seven += element

print("Cумма чисел из списка, сумма цифр которых делится нацело на 7: ", sum_of_digits_div_by_seven)

for i, el in enumerate(list_of_cubes):
    list_of_cubes[i] = el+17

print("К каждому элементу списка добавить 17: ", list_of_cubes)

sum_of_digits_div_by_seven = 0
for element in list_of_cubes:
    temp_sum = 0
    temp_sum += element // 1000000000
    temp_sum += (element % 1000000000) // 100000000
    temp_sum += (element % 100000000) // 10000000
    temp_sum += (element % 10000000) // 1000000
    temp_sum += (element % 1000000) // 100000
    temp_sum += (element % 100000) // 10000
    temp_sum += (element % 10000) // 1000
    temp_sum += (element % 1000) // 100
    temp_sum += (element % 100) // 10
    temp_sum += element % 10
    if temp_sum % 7 == 0:
        sum_of_digits_div_by_seven += element

print("Cумма новых чисел из списка, сумма цифр которых делится нацело на 7: ", sum_of_digits_div_by_seven)