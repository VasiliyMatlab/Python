from os import getpid
import socket
from time import sleep

# Открытие сокета и связывание его с дескриптором
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP = socket.gethostbyname(socket.gethostname())
PORT = 12333
listener.bind((IP, PORT))
listener.listen(0)

# Цикл приема клиентов
while True:
    # Прием клиента
    try:
        connection, address = listener.accept()
    except:
        break
    print(f'\nClient {address[0]}:{address[1]} accepted')

    # Цикл приема сообщений с подтверждением
    while True:
        data = connection.recv(1024).decode("utf8")
        if not data:
            print("EOF occured")
            print(f"Closing connection with client {address[0]}:{address[1]}")
            connection.close()
            break
        print(f"[{getpid()}] Message received\t({len(data)}):\t{data}")
        sleep(1)
        # Передаем ответ клиенту
        connection.send(data.encode("utf8"))
        print(f"[{getpid()}] Message sent\t({len(data)}):\t{data}")

# Закрытие сокета
print("\nClosing the server")
listener.close()
