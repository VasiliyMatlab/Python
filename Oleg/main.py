#!/usr/bin/python3

# Подключение библиотек
# Импортирование написанных функций
from functions import *
# Импортирование библиотеки для работы с текстовыми файлами
import json
# Импортирование библиотеки работы с матрицами
import numpy as np
# Импортирование библиотеки случайных чисел
import random as rnd
# Импортирование библиотеки специализированных вычислений
from scipy import interpolate

# Исходные данные
N = 1000                                        # кол-во гипотез дальности
n = range(0, N+1)                               # гипотезы дальности
maxSNR = 20                                     # максимальное ОСШ
dSNR = 0.5                                      # шаг изменения ОСШ
SNR = np.arange(0, maxSNR+dSNR, dSNR)           # ОСШ
newSNR = np.arange(0, maxSNR+dSNR/4, dSNR/4)    # интерполяция 'SNR'
E = 1000                                        # число экспериментов
experiments = zeros2D(len(SNR), E)              # массив экспериментов
minH = 3                                        # минимальное значение уровня порога
dH = 1                                          # шаг изменения уровня порога
maxH = 10                                       # максимальное значение уровня порога
H = np.arange(minH, maxH+dH, dH)                # уровень порога
Output = zeros2D(len(H), len(SNR))              # зависимость вероятности ПО от ОСШ
newOutput = zeros2D(len(H), len(newSNR))        # интерполяция 'Output'

# Рассчет
# Цикл по уровню порога
for z in range(len(H)):
    # Цикл по ОСШ
    for i in range(len(SNR)):
        # Цикл по экспериментам
        for j in range(E):
            # Формирование сигнала и порога
            # Сигнал
            NOISE_STD = (10 ** (-SNR[i]/10)) / 3            # СКО шума
            s = np.random.normal(0, NOISE_STD, size=N+1)    # шум
            target = rnd.randint(0, N)                      # положение цели
            s[target] = 1                                   # цель
            # Пороги
              # Постоянный порог  
            #Treshold = ones(N+1)
            #Treshold = list(float(k) for k in Treshold)
            #M = mean(s)
            #Treshold = list(H[z]*M*k for k in Treshold)
                # Скользящее среднее
            #Treshold = mov_mean(s, 50)
            #Treshold = list(H[z]*i for i in Treshold) 
                # CFAR-порог
            #Treshold = CFAR(s, 10, 10)
            #Treshold = list(H[z]*i for i in Treshold)

            # Обнаружение цели
            detect_s = list(s[k]>Treshold[k] for k in range(N+1))
            detect_n = list(detect_s[k]*n[k] for k in range(N+1))
            detect_s = list(detect_s[k]*s[k] for k in range(N+1))
            np.delete(detect_s, 0)
            np.delete(detect_n, 0)
            isrightdetection = True
            if detect_s == [] or not (target in detect_n):
                isrightdetection = False
            experiments[i][j] = isrightdetection
        # Вероятность ПО при определенном уровне порога и ОСШ
        Output[z][i] = sum(experiments[i]) * 100/E
    # Интерполяция характеристики обнаружения
    fun = interpolate.interp1d(SNR,Output[z])
    newOutput[z] = fun(newSNR)
    for k in range(len(newSNR)):
        if newOutput[z][k] > 100:
            newOutput[z][k] = 100
        if newOutput[z][k] < 0:
            newOutput[z][k] = 0
    newOutput[z] = newOutput[z].tolist()
    print("Завершено на "+str((z+1) * 100/len(H))+"%")

# Запись данных в файлы
# Запись ОСШ
#with open("SNR.txt","w") as fw:
#    json.dump(newSNR, fw)

# Запись характеристик обнаружения при постоянном пороге
#with open("Mean.txt","w") as fw:
#    json.dump(newOutput, fw)

# Запись характеристик обнаружения при скользящем среднем
#with open("Moving_Mean.txt","w") as fw:
#    json.dump(newOutput, fw)

# Запись характеристик обнаружения при CFAR-пороге
#with open("CFAR.txt","w") as fw:
#    json.dump(newOutput, fw)