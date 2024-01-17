import threading


threading.Thread(target=print, args=("Просто!", "но совершенно бесполезно!"), kwargs={"sep": "\n"}).start()

from datetime import datetime, date
print(date.today())
