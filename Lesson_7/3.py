"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
from random import randint
from statistics import median


def my_median(my_list):
    """
    Поиск медианы
    :param my_list: Исходный массив
    :return: Выводит медиану
    """
    len_list = len(my_list)
    sum_list = sum(my_list)
    avg = sum_list // len_list

    one_list = []
    two_list = []

    for val in my_list:
        if val < avg:
            one_list.append(val)
        else:
            two_list.append(val)

    # не исходный же массив)
    one_list.sort(), two_list.sort()
    one_len, two_len = len(one_list), len(two_list)

    # Идея такая: разбить исходный массив на два "равных" массива
    # тогда медиана будет, либо в первом массиве, последним элементом,
    # либо во втором первым элементом

    # код ниже извлекает значение медины из массива согластно
    # логике выше. Но эта логика работает, если длины массивов различны
    # на 1

    # но т.к. длина одного из массива может быть больше длины
    # другого на более чем 1, то нужны некоторые манипуляции(махинации)

    if one_len > two_len:
        index = one_len - two_len
        if index > 1:
            index = index // 2
            one_list = one_list[:one_len - index]

        one_list = one_list[::-1]
        return one_list[index - 1]
    else:
        index = two_len - one_len
        if index > 1:
            index = index // 2
            two_list = two_list[:two_len - index]
            return two_list[index]

        return two_list[index - 1]


m = randint(1, 500)
SIZE = 2 * m + 1

IN_LIST = [randint(0, 500) for i in range(SIZE)]

print(IN_LIST)
print(my_median(IN_LIST))
print(median(IN_LIST))


# Результат
# [136, 115, 299, 29, 439, 341, 189, 84, 108, 292, 315, 299, 489, 281, 362, 92 .... ]
# 265
# 265

# P.S.
# было сделано куча тестов, все они дали верный результат.
# если по какой-то причение "говнокод" выше не работает, то пес с ним.
# Медиана находится через сортировку исходного массива с извлечением
# среднего элемента.
