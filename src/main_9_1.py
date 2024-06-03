# Импортируем необходимые для работы библиотеки
import os
from typing import Optional


def directory_info(directory: Optional[str] = None, recurs_count: bool = False) -> dict:
    """Функция возвращает словарь с указанием количества файлов и папок в указанноу директории.
    Если директория не указана, по-умолчанию принимается директория нахождения текущего файла.
    Если в необязательном параметре 'recurs_count' передано значение 'True',
    выполняется рекурсивный подсчёт файлов и папок, включая вложенные,
    по-умолчанию значение необязательного параметра - 'False'"""
    # Определяем переменные для количества файлов и папок.
    files_count = 0
    folders_count = 0
    # В зависимости от переданного параметра директории определяем путь: указанный, либо текущий.
    if directory and os.path.isdir(directory):
        path = directory
    else:
        path = os.getcwd()
    # В зависимости от значения параметра 'recurs_count' ведём поверхностный (применяем os.csandir())
    # либо рекурсивный (применяем os.walk()) подсчёт файлов и папок.
    if not recurs_count:
        with os.scandir(path) as dir_info:
            for item in dir_info:
                if item.is_file():
                    files_count += 1
                elif item.is_dir():
                    folders_count += 1
    else:
        for _, folders, files in list(os.walk(path)):
            files_count += len(files)
            folders_count += len(folders)
    # Возвращаем результат в виде словаря заданного вида.
    return {"files": files_count, "folders": folders_count}
