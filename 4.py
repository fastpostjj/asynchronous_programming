import time
import threading

global T
T = 0

def task():
    global T
    T += 1
    print("Начало task " + str(T))
    time.sleep(15)
    print("Конец task " + str(T))


threads = []
for _ in range(10):
    thread = threading.Thread(target=task)
    thread.start()
    threads.append(thread)

start_time = time.perf_counter()
for thread in threads:
    thread.join(1)

print(time.perf_counter() - start_time)
    # new_tasks.append(threading.Thread(target=tasks[i], name=tasks[i].__name__, args=(args[i],)))
