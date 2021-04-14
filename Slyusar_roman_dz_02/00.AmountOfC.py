"""
Залание с вебинара:
    Посчитать колличество символов 'c' во всем списке space_ships
"""

space_ships = ['Challenger', 'Шаттл Дисковери', 'Буран']
char_for_search = 'с'  # Кирилличекая 'c'
counter = 0

for element in space_ships:
    counter += list(element).count(char_for_search)

print("Нашлось ", counter, " кириллических символов 'с'")
