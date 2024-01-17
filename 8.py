import threading
import time
from typing import Callable


"""
Функция принимает два вызываемых объекта: task - целевую
задачу на выполнение отдельным демоническим потоком и log_task - целевую
задачу логирования, которая должна выполниться, если выполнение task не
завершилось за отведенное время (и не должна, если task выполнился за
отведенное время). Контрольное время - третий аргумент функции.
"""


def task(*args):
    start_time = time.perf_counter()
    print("start task")
    time.sleep(4)
    print("end task", time.perf_counter() - start_time)


def log_task():
    print("log_task")


def thread_log(task: Callable, log_task: Callable, t_check: int | float) -> None:
    thread = threading.Thread(target=task, daemon=True)
    timer = threading.Timer(interval=t_check, function=log_task)
    start_time = time.perf_counter()
    thread.start()
    timer.start()
    thread.join(t_check)
    # if time.perf_counter() - start_time < t_check:
    timer.cancel()  # если тред отработает за меньшее или равное контрольному времени, таймер отменяется
    # если таймер начал выполняться, то нужно дождаться выполнения, так как логирование (в файл, например) может  являться блокирующей операцией
    timer.join()


t_check = 5
thread_log(task, log_task, t_check)
