import threading


var   = 0                   # Целевая переменная
mutex = threading.Lock()    # Мьютекс

# Потоковые функции
def minus():
    global var
    mutex.acquire() # Захват мьютекса
    loc = var
    print(f'min = {var}')
    loc -= 1
    var = loc
    mutex.release() # Высвобождение мьютекса

def plus():
    global var
    mutex.acquire() # Захват мьютекса
    loc = var
    print(f'plus = {var}')
    loc += 1
    var = loc
    mutex.release() # Высвобождение мьютекса

if __name__ == "__main__":
    # Создание потоков
    t1 = [threading.Thread(target=minus) for i in range(50)]
    t2 = [threading.Thread(target=plus) for i in range(50)]
    print('Threads created')

    # Старт потоков
    for i in range(50):
        t1[i].start()
        t2[i].start()
    print('Threads started')

    # Ожидание потоков
    for i in range(50):
        t1[i].join()
        t2[i].join()
    print('Threads joined')
