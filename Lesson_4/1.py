"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

from random import randint
from random import shuffle
from timeit import Timer


def change_places_min_max():
    """
    Функция меняет местами минимальный и
    максимальный элементы в массиве
    :return: Массив
    """

    my_list = list(set(randint(0, 30) for i in range(30)))
    # определим переменные, минимальному зададим максимальное значение,
    # а максимальному минимальное
    MIN_EL = 30
    MAX_EL = 0
    MIN_EL_KEY = 0
    MAX_EL_KEY = 0

    # перемешаем "массив", чтобы было интереснее
    shuffle(my_list)
    for key, value in enumerate(my_list):

        # поиск максимального и минимального
        # элементов и запоминаем их индексы
        # min() и max() неинтересны
        if value > MAX_EL:
            MAX_EL = value
            MAX_EL_KEY = key
        elif value < MIN_EL:
            MIN_EL = value
            MIN_EL_KEY = key

        # при случае, когда переменная MAX_EL равна максимальному значению
        # а MIN_EL минимальному - прекращаем поиск
        if MAX_EL == 30 and MIN_EL == 0:
            break
    # переставляем местами минимальное и максимальное значение
    my_list[MIN_EL_KEY], my_list[MAX_EL_KEY] = my_list[MAX_EL_KEY], my_list[MIN_EL_KEY]
    return my_list


t1 = Timer("change_places_min_max()", setup="from __main__ import change_places_min_max")
print('change_places_min_max', t1.timeit(number=1000), 'milliseconds')


def change_places_min_max_two():
    """
    Функция меняет местами минимальный и
    максимальный элементы в массиве
    :return: Массив
    """

    my_list = list(set(randint(0, 30) for i in range(30)))
    # определим переменные, минимальному зададим максимальное значение,
    # а максимальному минимальное

    MIN_EL = min(my_list)
    MAX_EL = max(my_list)

    shuffle(my_list)

    MIN_EL_KEY = my_list.index(MIN_EL)
    MAX_EL_KEY = my_list.index(MAX_EL)

    # переставляем местами минимальное и максимальное значение
    my_list[MIN_EL_KEY], my_list[MAX_EL_KEY] = my_list[MAX_EL_KEY], my_list[MIN_EL_KEY]
    return my_list


t2 = Timer("change_places_min_max_two()", setup="from __main__ import change_places_min_max_two")
print('change_places_min_max_two', t2.timeit(number=1000), 'milliseconds')

# Сложность похожа на линейную
# timeit на первую реализацию выдает результат change_places_min_max 0.07574980199933634 milliseconds
# timeit на вторую реализацию выдает результат change_places_min_max_two 0.07802550199994585 milliseconds
# Разница не в пользу стандартных функций, скорее всего
# из-за двойного поиска, т.е. сперва ищем элемент, а потом еще и индекс
