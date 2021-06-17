"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
    |--my_project
    |--settings
    |--mainapp
    |--adminapp
    |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?
"""
import os

SCRIPT_DIR = '01.starter.fs'

dir_names = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']

for name in dir_names:
    os.makedirs("{}/{}".format(SCRIPT_DIR, name), exist_ok=True)
    print("Создана папка {}/{}".format(SCRIPT_DIR, name))
