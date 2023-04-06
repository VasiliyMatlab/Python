#!/usr/bin/python3

# Ввод размера спирали
n = int(input())

if n == 1:
    print(1)
else:

    # Создаем двумерный массив
    M = [[0 for j in range(n)] for i in range(n)]
    i = 0

    # Заполняем верхнюю строку спирали
    for j in range(n):
        M[i][j] = i+j+1
    value = n  # текущее значение
    cur = n-1  # текущий оборот заполнения

    # Заполнение спирали
    while cur > 0:
        # Правая сторона
        for i in range(i+1, i+cur+1):
            value += 1
            M[i][j] = value
        # Нижняя сторона
        for j in range(j-1, j-cur-1, -1):
            value += 1
            M[i][j] = value
        cur -= 1
        # Левая сторона
        for i in range(i-1, i-cur-1, -1):
            value += 1
            M[i][j] = value
        # Верхняя сторона
        for j in range(j+1, j+cur+1):
            value += 1
            M[i][j] = value
        cur -= 1

    # Вывод спирали на экран
    for i in range(n):
        for j in range(n):
            print(M[i][j], end=' ')
        print()
