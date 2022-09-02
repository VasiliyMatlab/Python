# Импортирование функции вычисления мат. ожидания
from statistics import mean

# Формирование списка из нулей определенной длины
def zeros(n):
    listofzeros = [0] * n
    return listofzeros

# Формирование двумерного списка из нулей определенного размера
def zeros2D(m, n):
    listofzeros = [[0] * n] * m
    return listofzeros

# Формирование списка из единиц определенной длины
def ones(n):
    listofones = [1] * n
    return listofones

# Вычисление скользящего среднего
def mov_mean(s, window):
    Treshold = zeros(len(s))
    for i in range(len(s)):
        win = list(range(i-window, i+window+1))
        j = 0
        while j < len(win):
            if win[j] < 0 or win[j] >= len(s):
                win.pop(j)
                j -= 1
            j += 1
        Treshold[i] = mean(s[win[0]:win[-1]+1])
    return Treshold

# Вычисление CFAR-порога
def CFAR(s, guard, train):
    Treshold = zeros(len(s))
    for i in range(len(s)):
        win1 = list(range(i-guard-train, i-guard))
        win2 = list(range(i+guard+1, i+guard+train+1))
        j = 0
        while j < len(win1):
            if win1[j] < 0 or win1[j] >= len(s):
                win1.pop(j)
                j -= 1
            j += 1
        j = 0
        while j < len(win2):
            if win2[j] < 0 or win2[j] >= len(s):
                win2.pop(j)
                j -= 1
            j += 1
        if win1 != [] and win2 != []:
            Treshold[i] = mean(list(s[win1[0]:win1[-1]+1])+list(s[win2[0]:win2[-1]+1]))
        elif win1 != [] and win2 == []:
            Treshold[i] = mean(s[win1[0]:win1[-1]+1])
        elif win1 == [] and win2 != []:
            Treshold[i] = mean(s[win2[0]:win2[-1]+1])
        else:
            print("Error! Lists 'win1' and 'win2' are empty")
            exit()
    return Treshold

# Определение констант
MEAN_LEVEL      = 5
MOV_MEAN_LEVEL  = 5
CFAR_LEVEL      = 5
NOISE_STD       = 0.06