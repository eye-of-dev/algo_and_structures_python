"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

IN_LIST = [randint(0, 20) for i in range(20)]

print(f'Исходный массив {IN_LIST}')

# определим переменные, минимальному зададим максимальное значение,
# а максимальному минимальное
MIN_EL = 30
MAX_EL = 0
MIN_EL_KEY = 0
MAX_EL_KEY = 0

for key, value in enumerate(IN_LIST):
    #    поиск максимального и минимального
    #   элементов и запоминаем их индексы
    #  min() и max() неинтересны
    if value > MAX_EL:
        MAX_EL = value
        MAX_EL_KEY = key
    elif value < MIN_EL:
        MIN_EL = value
        MIN_EL_KEY = key

    # при случае, когда переменная MAX_EL равна максимальному значению
    # а MIN_EL минимальному - прекращаем поиск
    if MAX_EL == 20 and MIN_EL == 0:
        break

# В случае если максимальное число раньше минимального
if MIN_EL_KEY > MAX_EL_KEY:
    MIN_EL_KEY, MAX_EL_KEY = MAX_EL_KEY, MIN_EL_KEY


def list_sum(num_list):
    """
    Суммируем элементы списка рекурсивно
    :param num_list:
    :return:
    """
    if len(num_list) == 1:
        return num_list[0]
    return num_list[0] + list_sum(num_list[1:])


# В рекурсивную функциою передаем под[множество](спиcок),
# где индекс начального элемента сдвинут, чтобы не включать его в сумму
NEW_LIST = IN_LIST[MIN_EL_KEY + 1:MAX_EL_KEY]
print('Сумма элементов между минимальным и максимальным равна %d ' % list_sum(NEW_LIST))
