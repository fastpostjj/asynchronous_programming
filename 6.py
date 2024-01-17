import threading
from time import sleep

"""
Создайте пару сотен дочерних потоков и понаблюдайте за
работой операционной системы через диспетчер задач (win)
или системный монитор (lin) и выводом в консоль.
"""

def task():
    print(f"-starting task with {threading.current_thread().name}, {threading.active_count()=}")
    sleep(10)
    print(f"---end task with {threading.current_thread().name}")


threads = [threading.Thread(target=task) for _ in range(200)]
for thread in threads:
    thread.start()
    sleep(0.01)

print(f"{threading.active_count()=}")
print("END MAIN")