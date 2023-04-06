#!/usr/bin/python3

import threading

b = threading.Barrier(3)    # Барьер

# Потоковая функция
def fun():
    print(f'{threading.current_thread()} is waiting')
    b.wait()
    print(f'{threading.current_thread()} is ready')

if __name__ == "__main__":
    # Создание потоков
    t = [threading.Thread(target=fun) for i in range(2)]
    print('Threads created')

    # Старт потоков
    for i in range(2):
        t[i].start()
    print('Threads started')

    b.wait()

    # Ожидание потоков
    for i in range(2):
        t[i].join()
    print('Threads joined')
