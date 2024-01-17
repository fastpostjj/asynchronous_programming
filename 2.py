import threading
from time import sleep


def user_interface():
    while True:
        sleep(0.2)
        print("-", end="")


def task():
    while True:
        sleep(0.61)
        print("*", end="")


# Ваше решение
tasks = []

tasks.append(threading.Thread(target=user_interface))
tasks.append(threading.Thread(target=task))

for task in tasks:
    task.start()
