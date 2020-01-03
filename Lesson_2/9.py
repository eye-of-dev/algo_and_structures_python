"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def sum_numbers(numb, index):
    """ Функциоя возвращает сумму цифр числа
    :param numb: Число
    :param index: Счетчик
    :return: Сумма
    """
    if len(numb) == index:
        return 0
    return int(numb[index]) + int(sum_numbers(numb, index + 1))


STR_NUMBS = input('Введите числа через пробел:')
NUMB = 0
SUM_NUMB = 0

for i in STR_NUMBS.split(' '):
    sum_numbers = sum_numbers(i, 0)
    if sum_numbers > SUM_NUMB:
        NUMB = i
        SUM_NUMB = sum_numbers

print('Число %s, сумма цифр этого числа равна %s' % (NUMB, SUM_NUMB))
