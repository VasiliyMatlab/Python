#!/usr/bin/python3

from time import process_time
from os import getpid
from psutil import Process


start_time = process_time()

# ///////////////////////////////КОД///////////////////////////////////
i = 0
while i < 1000000:
    i += 1
print(i)
# ////////////////////////////КОНЕЦ КОДА///////////////////////////////

print('==============================================')
Memory = Process(getpid()).memory_info().rss / 1024
Time = process_time() - start_time
print('Memory:  %s Kbytes (%s Mbytes)' % (Memory, round(Memory / 1024, 2)))
print('Runtime: %s s (%s ms)' % (Time, round(Time * 1000, 1)))
