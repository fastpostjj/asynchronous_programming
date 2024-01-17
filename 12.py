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


class TwoTaskThread(threading.Thread):  # наследуем оригинальный класс Thread

    def __init__(self, task=None, args=()):
        super().__init__()
        self.task = task
        self.args = args

    def run(self):
        try:
            if self.task is not None:
                self.new_task(self.task(*self.args))
        finally:
            del self.task, self.args, self.new_task


def worker(*args) -> int:
    return sum(args)


def is_anton(text: str) -> bool:
    '''
    если в строке
    файла присутствует слово "anton" (необязательно рядом стоящие буквы,
    главное - наличие последовательности букв,
    разделенных в том числе пробелами) засеняем строку на
    !!! WARNING INFECTED !!!
    '''
    if re.search('a.*n.*t.*o.*n.*', text):
        return('!!! WARNING INFECTED !!!\n')
    return text

# def handler(n):
#     print(n)

filename_input = os.sep.join(["data", "words_0.txt"])
filename_output = os.sep.join(["data", "words_output.txt"])
text_output = ""
with open(filename_input, "r") as file:
    for line in file:
        text_output += is_anton(line)


with open(filename_output, "w") as file:
    file.write(text_output)
# my_thread = TwoTaskThread(worker, (filename,))

# print(my_thread.task)
# print(my_thread.new_task)
# print(my_thread.args)
# my_thread.start()