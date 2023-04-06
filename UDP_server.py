#!/usr/bin/python3

from os import getpid
import socket
from time import sleep

# Открытие сокета и связывание его с дескриптором
listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP = socket.gethostbyname(socket.gethostname())
PORT = 12444
listener.bind((IP, PORT))

# Цикл приема сообщений
while True:
    try:
        data, address = listener.recvfrom(1024)
    except:
        break
    data = data.decode("utf8")
    print(f"[{getpid()}] Message received ({len(data)}) from {address[0]}:{address[1]}:\t{data}")
    sleep(1)
    # Передаем ответ клиенту
    listener.sendto(data.encode("utf8"), address)
    print(f"[{getpid()}] Message sent\t ({len(data)}) to {address[0]}:{address[1]}:\t{data}")

# Закрытие сокета
print("\nClosing the server")
listener.close()
