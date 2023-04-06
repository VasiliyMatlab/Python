#!/usr/bin/python3

from time import sleep
import math

def rainbow(word):
    freq = (2 * math.pi) / len(word)
    amplitude = 255 / 2
    center = 255 / 2
    line = str()
    for i in range(len(word)):
        gShift = math.pi * 2 / 3
        bShift = math.pi * 4 / 3
        r = int(math.sin(freq * i) * amplitude + center)
        g = int(math.sin(freq * i + gShift) * amplitude + center)
        b = int(math.sin(freq * i + bShift) * amplitude + center)
        line += "\033[38;2;{};{};{};1m{} \033[38;2;255;255;255m".format(r, g, b, str(word[i]))
    return line

while True:
    print(rainbow("РАДУЖНАЯ НАДПИСЬ"))
    sleep(0.2)
