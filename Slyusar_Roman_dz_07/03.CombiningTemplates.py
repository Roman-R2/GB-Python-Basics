"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
«руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
templates, например:

|--my_project
...
|--templates
|   |--mainapp
|   |  |--base.html
|   |  |--index.html
|   |--authapp
|      |--base.html
|      |--index.html

Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
расположены в родительских папках (они играют роль пространств имён); предусмотреть
возможные исключительные ситуации; это реальная задача, которая решена, например, во
фреймворке django.
"""
import os
from distutils.dir_util import copy_tree

SCRIPT_DIR = '03.combining_templates.fs'

TEMPLATES_DIR = 'templates'


def make_folder(destination_folder, folder_name):
    os.makedirs("{}/{}".format(destination_folder, folder_name), exist_ok=True)


def create_fs_struct(destination_folder, fs_struct_dict):
    for folder_name, some_data in fs_struct_dict.items():
        if not some_data:
            make_folder(destination_folder, folder_name)
        else:
            make_folder(destination_folder, folder_name)
            if isinstance(some_data, list):
                for file_name in some_data:
                    if not isinstance(file_name, dict):
                        folder = "{}/{}/{}".format(destination_folder, folder_name, file_name)
                        open(folder, 'a').close()
                    if isinstance(file_name, dict):
                        folder = "{}/{}".format(destination_folder, folder_name)
                        create_fs_struct(folder, file_name)
            if isinstance(some_data, dict):
                folder = "{}/{}".format(destination_folder, folder_name)
                create_fs_struct(folder, some_data)


def collect_templates(source_directory, destination_directory):
    make_folder(source_directory, destination_directory)
    search_mask = "templates"
    template_folder = os.path.join(source_directory, destination_directory)
    for item in os.walk(source_directory):
        if item[0] != source_directory and search_mask in item[1]:
            from_folder = os.path.join(item[0], search_mask)
            copy_tree(from_folder, template_folder)


fs_struct = {
    'my_project': False,
    'settings': [
        '__init__.py',
        'dev.py',
        'prod.py'
    ],
    'mainapp': [
        '__init__.py',
        'models.py',
        'views.py',
        {'templates':
            {
                'mainapp': [
                    'base.html',
                    'index.html'
                ]
            }
        }
    ],
    'authapp': [
        '__init__.py',
        'models.py',
        'views.py',
        {'templates':
            {
                'authapp': [
                    'base.html',
                    'index.html'
                ]
            }
        }
    ]
}

# Создадим структуру из задания
create_fs_struct(SCRIPT_DIR, fs_struct)

# Соберем шаблоны в отдельную папку
collect_templates(SCRIPT_DIR, TEMPLATES_DIR)
