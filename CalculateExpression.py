## @brief Класс вычисления выражения в инфиксной нотации
#
#
class CalculateExpression:

    ## Применяемые скобки
    ## @var __BRACKETS
    #  @hideinitializer
    #  @private
    __BRACKETS   = {')': '(', ']': '[', '}': '{', '>': '<'}
    ## Приоритеты операций
    ## @var __OPERATIONS
    #  @hideinitializer
    #  @private
    __OPERATIONS = {'+': 1, '-': 1, '*': 2, '/': 2}

    ## Строка, хранящая в себе выражение
    ## @var string
    string = str()

    ## @brief Конструктор класса
    #
    #  @param[in,out] self Указатель на экземпляр класса
    #  @param[in] s Строка, содержащая выражение
    #
    def __init__(self, s: str) -> None:

        self.string = s

    ## @brief Определение типа символа
    #
    #  @param[in] self Указатель на экземпляр класса
    #  @param[in] s Символ, тип которого необходимого определить
    #  @return 'number' в случае числа; 'bracket' в случае скобки; 'operation' в случае операции
    #
    # @private
    def __which_type(self, s: str) -> str:

        if s.isnumeric():
            return 'number'
        if (s in self.__BRACKETS.keys()) or (s in self.__BRACKETS.values()):
            return 'bracket'
        if s in self.__OPERATIONS.keys():
            return 'operation'
        raise TypeError

    ## @brief Конвертация строки выражения в список
    #
    #  @param[in] self Указатель на экземпляр класса
    #  @param[in] s Строка, содержащая выражение
    #  @return Список, состоящий из элементов выражения
    #
    # @private
    def __convert_to_correct_list(self, s: str) -> list[str]:

        out = list()
        prev = self.__which_type(s[0])
        out.append(s[0])
        for i in range(1,len(s)):
            if s[i] == ' ':
                continue
            curr = self.__which_type(s[i])
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

    ## @brief Определяем, является ли строка правильной скобочной последовательностью
    #
    #  @param[in] self Указатель на экземпляр класса
    #  @param[in] s Список, содержащий элементы инфиксного выражения
    #  @return True в случае правильной скобочной последовательности; иначе False
    #
    # @private
    def __is_correct_brackets(self, s: list[str]) -> bool:

        stack = list()
        for el in s:
            if (el not in self.__BRACKETS.values()) or (el not in self.__BRACKETS.keys()):
                continue
            if el in self.__BRACKETS.values():
                stack.append(el)
                continue
            if stack:
                if stack[-1] == self.__BRACKETS[el]:
                    stack.pop()
                    continue
                return False
            return False
        return False if stack else True

    ## @brief Определяем, записано ли выражение в корректной инфиксной записи
    #
    #  @brief Инфиксное выражение записано корректно, если:
    #  1. Не стоит подряд двух операций
    #  2. Не стоит подряд двух операндов
    #  3. Выражение является правильной скобочной последовательностью
    #
    #  @param[in] self Указатель на экземпляр класса
    #  @param[in] s Список, содержащий элементы инфиксного выражения
    #  @return True в случае корректного инфиксного выражения; иначе False
    #
    # @private
    def __is_correct_infix(self, s: list[str]) -> bool:

        for i in range(len(s) - 1):
            if (s[i] in self.__OPERATIONS.keys()) and (s[i+1] in self.__OPERATIONS.keys()):
                return False
            if (s[i].isnumeric()) and (s[i+1].isnumeric()):
                return False
        return self.__is_correct_brackets(s)

    ## @brief Избавление от унарных операций с помощью добавления "0"
    #
    #  @param[in] self Указатель на экземпляр класса
    #  @param[in] s Список, содержащий элементы инфиксного выражения
    #  @return Список с добавленными "0", где это необходимо
    #
    # @private
    def __delete_unary(self, s: list[str]) -> list[str]:

        if s[0] == '-':
            s.insert(0, '0')
        i = 0
        while i < (len(s) - 1):
            if (s[i] in self.__BRACKETS.values()) and (s[i+1] == '-'):
                s.insert(i + 1, '0')
            i += 1
        return s

    ## @brief Конвертация инфиксной записи в префиксную
    #
    #  @brief Алгоритм конвертации:
    #  1. Операнд сразу попадает в ответ
    #  2. Операция выталкивает в ответ все операции с большим либо равным приоритетом и кладется в стек
    #  3. Открывающая скобка кладется в стек
    #  4. Закрывающая скобка выталкивает в ответ все операции до открывающей скобки, затем удаляет открывающую скобку
    #  5. В конце все операции выписываются в ответ
    #
    #  @param[in] self Указатель на экземпляр класса
    #  @param[in] s Список, содержащий элементы инфиксного выражения
    #  @return Список, содержащий элементы префиксного выражения
    #
    # @private
    def __infix_to_prefix(self, s: list[str]) -> list[str]:

        out = list()
        stack = list()
        for k in s:
            # Операнд
            if k.isnumeric():
                out.append(k)
                continue
            # Открывающая скобка
            if k in self.__BRACKETS.values():
                stack.append(k)
                continue
            # Закрывающая скобка
            if k in self.__BRACKETS.keys():
                while stack[-1] != self.__BRACKETS[k]:
                    out.append(stack.pop())
                stack.pop()
                continue
            # Операция
            if stack:
                while stack and \
                    (stack[-1] not in self.__BRACKETS.values()) and \
                    (self.__OPERATIONS[k] <= self.__OPERATIONS[stack[-1]]):
                    out.append(stack.pop())
                stack.append(k)
            else:
                stack.append(k)
        while stack:
            out.append(stack.pop())
        return out

    ## @brief Вычисление префиксного выражения
    #
    #  @param[in] self Указатель на экземпляр класса
    #  @param[in] s Список, содержащий элементы префиксного выражения
    #  @return Результат вычисления префиксного выражения
    #
    # @private
    def __calculate_prefix(self, s: list[str]) -> float:

        stack = list()
        for el in s:
            # Если число - кладем в стек
            if el.isnumeric():
                stack.append(float(el))
                continue
            # Операция - берем два числа из вершины стека,
            # совершаем операцию, кладем результат в стек
            num1 = float(stack.pop())
            num2 = float(stack.pop())
            match el:
                case '+':
                    stack.append(num2 + num1)
                case '-':
                    stack.append(num2 - num1)
                case '*':
                    stack.append(num2 * num1)
                case '/':
                    stack.append(num2 / num1)
                case _:
                    raise ValueError(el)
        return stack.pop()

    ## @brief Вычисление выражения
    #
    #  @param[in] self Указатель на экземпляр класса
    #  @return Результат вычисления выражения
    #
    def calculate_expression(self) -> float:

        l = self.__convert_to_correct_list(self.string)
        if not self.__is_correct_infix(l):
            raise ValueError
        li = self.__delete_unary(l)
        lp = self.__infix_to_prefix(li)
        return self.__calculate_prefix(lp)

if __name__ == "__main__":
    out = CalculateExpression(input())
    print(out.calculate_expression())
