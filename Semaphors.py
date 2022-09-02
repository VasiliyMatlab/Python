import threading
from time import sleep


# Семафоры
sem1 = threading.Semaphore(0)
sem2 = threading.Semaphore(0)

# Потоковые функции
def waiter():
    sleep(1)
    # Ожидание семафора 2
    sem2.acquire()
    print('Waiter work!')

def signaler1():
    sleep(3)
    # Высвобождение семафора 1
    sem1.release()
    print('Signaler 1 work!')

def signaler2():
    sleep(2)
    # Ожидание семафора 1
    sem1.acquire()
    # Высвобождение семафора 2
    sem2.release()
    print('Signaler 2 work!')


if __name__ == "__main__":
    # Создание потоков
    t1 = threading.Thread(target=waiter)
    t2 = threading.Thread(target=signaler1)
    t3 = threading.Thread(target=signaler2)
    print('Threads created')

    # Старт потоков
    t1.start()
    t2.start()
    t3.start()
    print('Threads started')

    # Ожидание потоков
    t1.join()
    t2.join()
    t3.join()
    print('Threads joined')
