"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

IN_LIST = [randint(0, 20) for i in range(20)]


# не хочется использовать сортировку и вытаскивать 2 первых элемента


def search_min_element(my_list):
    """
    Функция поиска минимального элемента
    :param my_list:
    :return:
    """
    min_el = 20
    for value in my_list:

        # поиск максимального и минимального
        # элементов и запоминаем их индексы
        # min() и max() неинтересны
        if value < min_el:
            min_el = value

        # при случае, когда переменная MIN_EL
        # минимальному значению- прекращаем поиск
        if min_el == 0:
            break

    return min_el


print(f'Исходный массив {IN_LIST}')

MIN_EL_ONE = search_min_element(IN_LIST)
# удаляем первый минимальный элемент, чтобы найти второй инмальный
IN_LIST.remove(MIN_EL_ONE)
MIN_EL_TWO = search_min_element(IN_LIST)

print('Два минимальных значения в списке: первое - %d, второе - %d' % (MIN_EL_ONE, MIN_EL_TWO))
