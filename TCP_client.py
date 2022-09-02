from os import getpid
import socket
from random import randint, choice
import string
from time import sleep

# Открытие сокета и установление соединения
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
PORT = 12333
try:
    connection.connect((IP, PORT))
except:
    print("Connection failed")
    exit()
print(f"Connected to server {IP}:{PORT}")

# Цикл передачи сообщений с приемом подтверждения от сервера
cnt = randint(2,20)
print(f"Number of messages: {cnt}")
while cnt:
    # Формирование сообщения
    length = randint(1,40)
    buf = list()
    for i in range(length):
        tmp = choice(string.ascii_letters + string.digits)
        buf.append(tmp)
    buf = ''.join(buf)
    # Передаем информацию на сервер
    connection.send(buf.encode("utf8"))
    print(f"[{getpid()}] Message sent\t({length}):\t{buf}")
    # Получаем информацию от сервера
    buf = connection.recv(1024).decode("utf8")
    if not buf:
        print("EOF occured")
        break
    print(f"[{getpid()}] Message received\t({len(buf)}):\t{buf}")
    sleep(1)
    cnt -= 1

# Закрытие сокета
print("Closing connection")
connection.close()
