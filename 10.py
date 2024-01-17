import threading
import time


"""
Напишите функцию callback_handler, которая запускает целевую задачу (например,
выполнение запроса), а в случае получения результата за заданное время
запускает дополнительную задачу (например, сохранение результата запроса).

Напишите функцию, которая выполняет целевую задачу task и задачу дополнительной
обработки callback_task в отдельных потоках. При этом известно, что признаком
успешного выполнения целевой задачи является переменная result, которая в
случае успеха принимает значение True (False - значение по умолчанию).
Переменная result доступна в глобальной области видимости.

Целевая функция task  принимает аргументы args в виде кортежа значений,
поэтому при создании потока достаточно указать threading.
Thread(target=task, args=args, ....). Функция callback_task  работает
без аргументов и она выполняется не мгновенно, сохранение результатов
занимает небольшое время!

Для ограничения ожидания успешного выполнения целевой задачи ограничьте время
работы потока целевой задачи 0.3 секундой (считаем, что за 300 мс. (или
раньше) запрос точно будет успешно получен, если нет - дальнейшие ожидания
нужно прекратить). Если result True, потоком - таймером выполняем
дополнительную задачу и дожидаемся ее завершения, если нет - не выполняем
(результат не получен, нечего сохранять).

Решите задачу без расчета времени выполнения, используйте поток, поток-таймер
и методы join, start, cancel. Во временных уставках допускается погрешность в 0.05 секунды
"""


def task(*args):
    start_time = time.perf_counter()
    print("start task")
    time.sleep(4)
    print("end task", time.perf_counter() - start_time)
    result = True
    return result


def callback_task():
    print("callback_task")


def callback_handler(args, t_check: int | float):
    new_thread = threading.Thread(target=task, args=(args,), name="Thread", daemon=True)
    timer = threading.Timer(t_check, callback_task)
    timer.name = "Timer"
    new_thread.start()
    timer.start()
    new_thread.join(t_check)
    if not new_thread.is_alive():
        timer.cancel()
    # timer.join()


t_check = 3
args = 3
test_thread_timer(args, t_check)
