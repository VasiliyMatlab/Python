#!/usr/bin/python3

with open('code.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
string = list(line)
i = 0
with open('decode.txt', 'w') as ouf:
    while i < len(string):
        for j in range(i+1, len(string)):
            if ((string[j] != '0') and (string[j] != '1')
                    and (string[j] != '2') and (string[j] != '3')
                    and (string[j] != '4') and (string[j] != '5')
                    and (string[j] != '6') and (string[j] != '7')
                    and (string[j] != '8') and (string[j] != '9')):
                j -= 1
                break
        j -= i
        num = int(''.join(string[i+1:i+j+1]))
        for k in range(num):
                ouf.write(string[i])
                # print(string[i],end='')
        i += j+1
