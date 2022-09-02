# Подключение библиотек
# Импортирование библиотеки построения графиков
import matplotlib.pyplot as plt
# Импортирование библиотеки для работы с текстовыми файлами
import json

# Чтение данных из файлов
# Чтение ОСШ
with open("SNR.txt","r") as fr:
    SNR = json.load(fr)

# Чтение характеристик обнаружения постоянного порога
with open("Mean.txt","r") as fr:
    mean = json.load(fr)

# Чтение характеристик обнаружения скользящего среднего
with open("Moving_Mean.txt","r") as fr:
    moving_mean = json.load(fr)

# Чтение характеристик обнаружения CFAR-порога
with open("CFAR.txt","r") as fr:
    cfar = json.load(fr)

# Построение графиков
plt.subplot(2,2,1)
plt.plot(SNR, mean)
plt.title("Mean")
plt.xlim([0, 20])
plt.grid()
plt.xlabel("ОСШ, дБ")
plt.ylabel("Вероятность правильного обнаружения, %")
plt.legend(labels=("H = 3","H = 4","H = 5","H = 6","H = 7","H = 8","H = 9",
    "H = 10",),loc="outside center right")
plt.subplot(2,2,2)
plt.plot(SNR, moving_mean)
plt.title("Moving mean")
plt.xlim([0, 20])
plt.grid()
plt.xlabel("ОСШ, дБ")
plt.ylabel("Вероятность правильного обнаружения, %")
plt.legend(labels=("H = 3","H = 4","H = 5","H = 6","H = 7","H = 8","H = 9",
    "H = 10",),loc="outside center right")
plt.subplot(2,2,3)
plt.plot(SNR, cfar)
plt.title("CFAR")
plt.xlim([0, 20])
plt.grid()
plt.xlabel("ОСШ, дБ")
plt.ylabel("Вероятность правильного обнаружения, %")
plt.legend(labels=("H = 3","H = 4","H = 5","H = 6","H = 7","H = 8","H = 9",
    "H = 10",),loc="outside center right")