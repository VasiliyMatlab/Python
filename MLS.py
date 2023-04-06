#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def xcorr(x: np.ndarray) -> np.ndarray:
    return np.correlate(x, x, mode = 'full')

def zeros(m: int) -> list:
    return [0] * m

def hex2bin(a: str, n=0) -> str:
    if n:
        b = bin(int(a, 16))[2:].zfill(n)
    else:
        b = bin(int(a, 16))[2:]
    return b

def CFAR(Input: np.ndarray, guard: int, train: int, gain: float, value: float, mode: str) -> np.ndarray:
    if mode != "sum" and mode != "mean":
        raise ValueError
    Treshold = np.array(zeros(len(Input)), float)
    for i in range(len(Input)):
        win = list(range(i-guard-train, i-guard)) + list(range(i+guard+1, i+guard+train+1))
        j = 0
        while j < len(win):
            if win[j] < 0 or win[j] >= len(Input):
                win.remove(win[j])
                continue
            j += 1
        tmp = list()
        for j in win:
            tmp.append(Input[j])
        if mode == "sum":
            Treshold[i] = np.sum(tmp)
        else:
            Treshold[i] = np.mean(tmp)
    Treshold = gain*Treshold + value
    return Treshold

def Generate_MLS(mpoly: str, minit: str) -> np.ndarray:
    mpoly = hex2bin(mpoly)
    N = len(mpoly) - 1
    minit = hex2bin(minit,N)
    if (mpoly[N] == '0'):
        raise ValueError
    Signal = np.array(zeros(2**N-1), float)
    reg = [-1] * N
    for i in range(N):
        if minit[N-i-1] == '1':
            reg[i] = 1
    pos = list()
    for i in range(N-1,-1,-1):
        if mpoly[i] == '1':
            pos.append(N-i-1)
    for i in range(2**N-1):
        Signal[i] = reg[N-1]
        saveBit = 1
        for j in pos:
            saveBit *= reg[j]
        reg[1:N] = reg[0:N-1]
        reg[0] = saveBit
    return Signal


mpoly = '0x25'
minit = '0x56'
Sig = Generate_MLS(mpoly, minit)
print(Sig)
R = np.abs(xcorr(Sig))
#R = R + np.abs(50*np.random.normal(0,1,len(R)))
# R[4094] = R[4094] / 16
x = np.array(list(range(len(R))), int)
Treshold = CFAR(R,3,5,1,0,"sum")
#Treshold = CFAR(R,3,5,5,0,"mean")

targs = (R > Treshold) * R
x1 = np.ndarray([], int)
for i in range(len(targs)):
    if targs[i]:
        x1 = np.append(x1, x[i])
x1 = np.delete(x1, 0)
i = 0
while i < len(targs):
    if not targs[i]:
        targs = np.delete(targs, i)
        continue
    i += 1

plt.plot(x, R, "-", label="Signal")
plt.plot(x, Treshold, "k--", label="Treshold")
plt.scatter(x1, targs, c="r", label="Detection", linewidth=1)
plt.grid(True)
plt.legend()
plt.show()
