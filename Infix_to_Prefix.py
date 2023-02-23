BRACKETS   = {')': '(', ']': '[', '}': '{', '>': '<'}
OPERATIONS = {'+': 1, '-': 1, '*': 2, '/': 2}

# Определение типа символа
def which_type(s: str) -> str:
    if s.isnumeric():
        return 'digit'
    if (s in BRACKETS.keys()) or (s in BRACKETS.values()):
        return 'bracket'
    if s in OPERATIONS.keys():
        return 'operation'
    raise TypeError

# Конвертация строки выражения в список
def convert_to_correct_list(s: str) -> list:
    out = list()
    prev = which_type(s[0])
    out.append(s[0])
    for i in range(1,len(s)):
        if s[i] == ' ':
            continue
        curr = which_type(s[i])
        if (curr == 'bracket') or (curr == 'operation'):
            out.append(s[i])
            prev = curr
            continue
        if (curr == prev):
            out.append(out.pop() + s[i])
            continue
        out.append(s[i])
        prev = curr
    return out

# Определяем, является ли строка правильной скобочной последовательностью
def is_correct_brackets(s: list) -> bool:
    stack = list()
    for el in s:
        if (el not in BRACKETS.values()) or (el not in BRACKETS.keys()):
            continue
        if el in BRACKETS.values():
            stack.append(el)
            continue
        if stack:
            if stack[-1] == BRACKETS[el]:
                stack.pop()
                continue
            return False
        return False
    return False if stack else True

# Определяем, записано ли выражение в корректной инфиксной записи
# Инфиксное выражение записано корректно, если:
# 1. Не стоит подряд двух операций
# 2. Не стоит подряд двух операндов
# 3. Выражение является правильной скобочной последовательностью
def is_correct_infix(s: list) -> bool:
    for i in range(len(s) - 1):
        if (s[i] in OPERATIONS.keys()) and (s[i+1] in OPERATIONS.keys()):
            return False
        if (s[i].isnumeric()) and (s[i+1].isnumeric()):
            return False
    return is_correct_brackets(s)

# Избавиться от унарных операций, добавив "0"
def delete_unary(s: list) -> list:
    if s[0] == '-':
        s.insert(0, '0')
    i = 0
    while i < (len(s) - 1):
        if (s[i] in BRACKETS.values()) and (s[i+1] == '-'):
            s.insert(i + 1, '0')
        i += 1
    return s

# Конвертация инфиксной записи в префиксную:
# 1. Операнд сразу попадает в ответ
# 2. Операция выталкивает в ответ все операции с большим либо равным приоритетом и кладется в стек
# 3. Открывающая скобка кладется в стек
# 4. Закрывающая скобка выталкивает в ответ все операции до открывающей скобки, затем удаляет открывающую скобку
# 5. В конце все операции выписываются в ответ
def infix_to_prefix(s: list) -> list:
    out = list()
    stack = list()
    for k in s:
        # Операнд
        if k.isnumeric():
            out.append(k)
            continue
        # Открывающая скобка
        if k in BRACKETS.values():
            stack.append(k)
            continue
        # Закрывающая скобка
        if k in BRACKETS.keys():
            while stack[-1] != BRACKETS[k]:
                out.append(stack.pop())
            stack.pop()
            continue
        # Операция
        if stack:
            while (stack[-1] not in BRACKETS.values()) and (OPERATIONS[k] <= OPERATIONS[stack[-1]]):
                out.append(stack.pop())
            stack.append(k)
        else:
            stack.append(k)
    while stack:
        out.append(stack.pop())
    return out

s = convert_to_correct_list(input())
if not is_correct_infix(s):
    raise ValueError
s = delete_unary(s)
print(infix_to_prefix(s))
