from time import sleep
from threading import Thread

# Потоковая функция
def hellofunc():
    print('Hello from thread!')
    sleep(3)

if __name__ == "__main__":
    thr = Thread(target=hellofunc)  # Создаем поток
    thr.start()                     # Старт потока
    print('Hello from main!')
    thr.join()                      # Ждем завершения потока
    print('OK. Go next')

