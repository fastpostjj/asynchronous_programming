from time import sleep, perf_counter
"""
Тимлид решает, что на каждый запрос надо отводить не более 1.5 секунды.
Вместо заголовков для ресурсов, ответ от которых превышает этот лимит,
необходимо заполнять строковым значением "no_response".
 на печать должно быть выведено:
bing.com-ok, google.ru-ok, mail.ru-no_response, ya.ru-ok, yahoo.com-no_response
"""

headers_stor = {}
sources = ["bing.com",
           "google.ru",
           "yahoo.com",
           "mail.ru",
           "ya.ru"]
start_time = perf_counter()  # запускаем отсчет времени проверки решения

def get_request_header(url: str):
    # моделируем различное время ответа от ресурсов
    # start_time = perf_counter()
    if url == "yahoo.com":
        sleep(10)
    elif url == "mail.ru":
        sleep(1.8)
    elif url == "google.ru":
        sleep(0.2)
    else:
        sleep(1.4)
    headers_stor[url] = "ok"
    # print("finish", url, perf_counter() - start_time)


import threading

# Ваше решение
tasks = []
for source in sources:
    headers_stor[source] = "no_response"
    task = threading.Thread(target=get_request_header, args=(source,), daemon=True)
    tasks.append(task)
    task.start()
sleep(1.5)



assert perf_counter() - start_time <= 2  # проверка того, что решение выполняется не более 2 секунд

print(", ".join(f'{k}-{v}' for k, v in sorted(headers_stor.items())))
