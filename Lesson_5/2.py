"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def sum_hex(one_arg, two_arg):
    """
    Функция суммирования шестнадцатеричных чисел
    :param one_arg: Первое значение
    :param two_arg: Второе значение
    :return:
    """
    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0

    if len(two_arg) > len(one_arg):
        one_arg, two_arg = deque(two_arg), deque(one_arg)

    else:
        one_arg, two_arg = deque(one_arg), deque(two_arg)

    while one_arg:

        if two_arg:
            res = hex_num[one_arg.pop()] + hex_num[two_arg.pop()] + transfer

        else:
            res = hex_num[one_arg.pop()] + transfer

        transfer = 0

        if res < 16:
            result.appendleft(hex_num[res])

        else:
            result.appendleft(hex_num[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    return list(result)


def mult_hex(one_arg, two_arg):
    """
    Функция умножения двух шестнадцатеричных чисел
    :param one_arg: Первое значение
    :param two_arg: Второе значение
    :return:
    """
    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    spam = deque([deque() for _ in range(len(two_arg))])

    one_arg, two_arg = one_arg.copy(), deque(two_arg)

    for i in range(len(two_arg)):
        temp_var = hex_num[two_arg.pop()]

        for j in range(len(one_arg) - 1, -1, -1):
            spam[i].appendleft(temp_var * hex_num[one_arg[j]])

        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(hex_num[res])

        else:
            result.appendleft(hex_num[res % 16])
            transfer = res // 16

    if transfer:
        result.appendleft(hex_num[transfer])

    return list(result)


ONE_VAR = list(input('Введите 1-е шестнадцатиричное число: ').upper())
TWO_VAR = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(ONE_VAR, '+', ONE_VAR, '=', sum_hex(ONE_VAR, TWO_VAR))

print(ONE_VAR, '*', TWO_VAR, '=', mult_hex(ONE_VAR, TWO_VAR))
