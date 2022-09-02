def IsParent(obj,class1,class2):
    if obj[class2] == ['None']:
        return 'No'
    elif class1 in obj[class2]:
        return 'Yes'
    else:
        for parent in obj[class2]:
            if IsParent(obj,class1,parent) == 'Yes':
                return 'Yes'
        else:
            return 'No'

n = int(input())
obj = dict()
for i in range(n):
    str = input().split()
    if len(str) == 1:
        if str[0] not in obj.keys():
            obj[str[0]] = ['None']
    else:
        if str[0] not in obj.keys():
            obj[str[0]] = str[2:]
        else:
            if obj[str[0]] == ['None']:
                obj[str[0]].clear()
            obj[str[0]].extend(str[2:])
        str.reverse()
        str.pop()
        str.pop()
        str.reverse()
        for j in str:
            if j not in obj.keys():
                obj[j] = ['None']
temp = list()
for i in obj.keys():
    j = 0
    while j < len(obj[i]):
        temp.clear()
        temp.extend(obj[i])
        var = temp.pop(j)
        if var in temp:
            obj[i].clear()
            obj[i].extend(temp)
        else:
            j += 1
print('------------------------')
m = int(input())
errors = list()
log = list()
for i in range(m):
    errors.append(input())
    if i != 0:
        for j in range(i):
            if (IsParent(obj,errors[j],errors[i]) == 'Yes') or (errors[i] == errors[j]):
                log.append(errors[i])
                break
print('------------------------')
if len(log) == 1:
    print(log[0])
else:
    print(log[0])
    for i in range(len(log)):
        if (i != 0) and (log[i] not in log[0:i-1]):
            print(log[i])