import threading


class TwoTaskThread(threading.Thread):  # наследуем оригинальный класс Thread

    def __init__(self, task=None, new_task=None, args=()):
        super().__init__()
        self.new_task = new_task
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


def handler(n):
    print(n)


my_thread = TwoTaskThread(worker, handler, (1, 2, 3))
print(my_thread.task)
print(my_thread.new_task)
print(my_thread.args)
my_thread.start()
