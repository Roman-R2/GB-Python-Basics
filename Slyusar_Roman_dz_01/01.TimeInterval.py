"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOURS = 3600
SECONDS_PER_DAY = 86400

minutes = 0
seconds = 0
hours = 0

input_data = input("Введите промежуток времени в секундах: ")

if not input_data:
    print("[ERROR 1] - Вы ничего не ввели!")
    exit()

for i in range(len(input_data)):
    if not input_data[i].isdigit():
        print("[ERROR 2] - Вы ввели данные в неправильном формате!")
        exit()

duration = int(input_data)

if duration <= SECONDS_PER_MINUTE:

    print(duration, "сек")
elif duration < SECONDS_PER_HOURS:
    minutes = duration // SECONDS_PER_MINUTE
    seconds = duration % SECONDS_PER_MINUTE
    print(minutes, "мин", seconds, "сек")
elif duration < SECONDS_PER_DAY:
    hours = duration // SECONDS_PER_HOURS
    minutes = (duration % SECONDS_PER_HOURS) // SECONDS_PER_MINUTE
    seconds = duration % SECONDS_PER_MINUTE
    print(hours, "часов", minutes, "мин", seconds, "сек")
else:
    print("Меня пока не научили обрабатывать такие значения :)")

