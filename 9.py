import threading
import time


"""
Воспроизведем функционал логирования отдельным потоком - таймером по простому
условию: если рабочий поток не выполнил свою целевую задачу вовремя (не
выполнил за контрольное время), то выполняется вспомогательный поток с
целевой задачей логирования. Если выполнил - запуск потока логирования
отменяется. Решение оформить в виде функции с именем
test_thread_timer(t_check), где t_check - контрольное значение времени.

В тестирующей системе определена целевая функция рабочего потока executer,
функция логирования logging.

В функции test_thread_timer Вам необходимо:

Создать и запустить рабочий поток с именем (атрибут name) Thread (англ).
Поставить на запуск с ожиданием t_check вспомогательный поток логирования
с именем Timer (англ.).
Ожидать завершения рабочего потока.
Если время между окончанием завершения и запуском рабочего потока не
превышает контрольного значения - отменить запуск потока логирования.
"""


def executer(*args):
    start_time = time.perf_counter()
    print("start executer")
    time.sleep(4)
    print("end executer", time.perf_counter() - start_time)


def logging():
    print("logging")


def test_thread_timer(t_check: int | float):
    new_thread = threading.Thread(target=executer, name="Thread", daemon=True)
    timer = threading.Timer(t_check, logging)
    timer.name = "Timer"
    new_thread.start()
    timer.start()
    new_thread.join(t_check)
    if not new_thread.is_alive():
        timer.cancel()
    # timer.join()


t_check = 3
test_thread_timer(t_check)
