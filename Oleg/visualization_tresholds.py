#!/usr/bin/python3

# Подключение библиотек
# Импортирование написанных функций
from functions import *
# Импортирование библиотеки построения графиков
import matplotlib.pyplot as plt
# Импортирование библиотеки работы с матрицами
import numpy as np

# Рассчет
# Вычисление сигнала
N = 1000            # кол-во гипотез дальности
n = range(0,N+1)    # гипотезы дальности
# Генерация шума
s = abs(np.random.normal(0, NOISE_STD, size=N+1))   # шум
s[round(N/2)] = 1                                   # цель
# Вычисление порога
    # Постоянный порог
# Treshold = ones(N+1)
# Treshold = list(float(i) for i in Treshold)
# Treshold = list(MEAN_LEVEL*mean(s)*i for i in Treshold)
    # Скользящее среднее
# Treshold = mov_mean(s, 50)
# Treshold = list(MOV_MEAN_LEVEL*i for i in Treshold) 
    # CFAR-порог
Treshold = CFAR(s, 10, 10)
Treshold = list(CFAR_LEVEL*i for i in Treshold) 

# Построение графика
plt.plot(n, s, color='blue', label="Сигнал")
plt.plot(n, Treshold, color='red', label="Порог")
plt.grid()
plt.xlabel("Гипотезы дальности")
plt.ylabel("Принятый сигнал")
plt.legend()
plt.xlim([0, N])
plt.show()