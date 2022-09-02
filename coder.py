st = input()
string = list(st)
s = [0]
i = 0
if len(string) != 1:
    while i < (len(string)):
        if i == (len(string)-1):
            if string[i] != string[i-1]:
                s += string[i]
                s += ['1']
            i += 1
        else:
            s += string[i]
            if string[i] == string[i+1]:
                num = 1
                j = i
                while j < (len(string)-1):
                    if (string[j] == string[j+1]):
                        num += 1
                    else:
                        break
                    j += 1
                s += [str(num)]
                i += num
            else:
                s += ['1']
                i += 1
else:
    s += string[0]
    s += ['1']
del s[0]
with open('code.txt', 'w') as ouf:
     ouf.write(''.join(s))
