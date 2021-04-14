"""
Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
Вывести все склонения для проверки.
"""

input_data = input("Введите число: ")

if not input_data:
    print("[ERROR 1] - Вы ничего не ввели!")
    exit()

for i in range(len(input_data)):
    if not input_data[i].isdigit():
        print("[ERROR 2] - Вы ввели данные в неправильном формате!")
        exit()

int_input_data = int(input_data)

if int_input_data > 20:
    print("[ERROR 3] - Вы ввели число, которое больше 20!")

if int_input_data == 1:
    print(int_input_data, "процент")
elif 2 <= int_input_data <= 4:
    print(int_input_data, "процента")
elif 5 <= int_input_data <= 20:
    print(int_input_data, "процентов")
else:
    print("Произошло что-то невообразимое!!!")