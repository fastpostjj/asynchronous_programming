import threading
from time import sleep


def get_inform():
    print(f"{threading.current_thread().name=}")
    print(f"{threading.current_thread().ident=}")
    print(f"{threading.current_thread().native_id=}")
    print(f"{threading.get_ident()=}")
    print(f"{threading.get_native_id()=}")
    print("---------------")
    sleep(100)


thr = [threading.Thread(target=get_inform) for _ in range(3)]
[t.start() for t in thr]
sleep(1)
print(threading.enumerate()) # возвращает список всех активных (живых) потоков
for t in threading.enumerate():
    print(f"{t.name=}")
    print(f"{t.ident=}")
    print(f"{t.native_id=}")