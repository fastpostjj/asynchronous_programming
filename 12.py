"""
поток, который создает копию переданного файла, в котором происходит замена
текста на предупреждающее сообщение (задается пользователем) если в строке
файла присутствует слово "anton" (необязательно рядом стоящие буквы, главное
 - наличие последовательности букв, разделенных в том числе пробелами).

Например, в заданном файле встречается строка:
Lorem ipsum dolor sit amet consectetur adipiscing elit Cras euismod ex a ante sollicitudin,

Тогда вся строка заменяется на предупреждающее сообщение, например
"!!! WARNING INFECTED !!!".
"""

import threading
import os
import re
import shutil
from time import perf_counter


class TwoTaskThread(threading.Thread):  # наследуем оригинальный класс Thread

    def __init__(self, filename_input, filename_output, task=None, args=()):
        super().__init__()
        self.task = task
        self.args = args
        self.filename_input = filename_input
        self.filename_output = filename_output

    def run(self, ):
        text_output = ""
        with open(self.filename_input, "r") as file:
            for line in file:
                text_output += is_anton(line)
        with open(self.filename_output, "w") as file:
            file.write(text_output)


def is_anton(text: str) -> bool:
    '''
    если в строке
    файла присутствует слово "anton" (необязательно рядом стоящие буквы,
    главное - наличие последовательности букв,
    разделенных в том числе пробелами) заменяем строку на
    !!! WARNING INFECTED !!!
    '''
    if re.search('a.*n.*t.*o.*n.*', text):
        return '!!! WARNING INFECTED !!!\n'
    return text

def check_file(filename_input, filename_output):
    text_output = ""
    with open(filename_input, "r") as file:
        for line in file:
            text_output += is_anton(line)
    with open(filename_output, "w") as file:
        file.write(text_output)


def asynchronous():
    time_start = perf_counter()
    filename_input = os.sep.join(["data", "words_0.txt"])
    threads = []

    # Копируемя исходный файл  и запускаем проверку текста в отдельных потоках
    for i in range(50):
        filename = os.sep.join(["data", "new_file" + str(i) + ".txt"])
        shutil.copy2(filename_input, filename)
        filename_output = os.sep.join(["data", "words_output" + str(i) + ".txt"])
        my_thread = TwoTaskThread(
                filename,
                filename_output
                )
        threads.append(my_thread)
        my_thread.start()
    for thread in threads:
        thread.join()
    time_end = perf_counter() - time_start
    print(time_end)

    # Записываем результат в файл
    with open(os.sep.join(["result", "result_threading.txt"]), "a") as file:
        file.write(str(time_end) +"\n")


def synchronous():
    time_start = perf_counter()
    filename_input = os.sep.join(["data", "words_0.txt"])

    # Копируемя исходный файл  и запускаем проверку текста в отдельных потоках
    for i in range(50):
        filename = os.sep.join(["data", "new_file" + str(i) + ".txt"])
        shutil.copy2(filename_input, filename)
        filename_output = os.sep.join(["data", "words_output" + str(i) + ".txt"])
        check_file(filename_input, filename_output)
    time_end = perf_counter() - time_start
    print(time_end)

    # Записываем результат в файл
    with open(os.sep.join(["result", "result_synchronous.txt"]), "a") as file:
        file.write(str(time_end) +"\n")


def main():
    # Сравниваем работу функции проверки и замены фразы
    # в текстовом файле в синхронном и асинхронном режимах
    for i in range(20):
        synchronous()
        delete_all_files()

        asynchronous()
        delete_all_files()

def delete_all_files():
    """
    Удаляем все файлы в каталоге data, кроме исходного - words_0.txt
    """
    filename_input = os.sep.join(["data", "words_0.txt"])
    file_list = os.listdir("data")
    for file in file_list:
        file_path = os.sep.join(["data", file])
        if os.path.isfile(file_path) and file_path != filename_input:
            os.remove(file_path)


main()
