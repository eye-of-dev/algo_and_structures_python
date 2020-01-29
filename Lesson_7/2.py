"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import uniform


def merge_sort(my_list):
    """
    Функция сортировки методом слияния
    :param my_list: Исходный массив
    :return: Выводит отсортированный результат
    """

    def merge(left, right):
        res = []
        i, j = 0, 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res.extend(left[i:] if i < len(left) else right[j:])

        return res

    def div_half(my_list):

        if len(my_list) == 1:
            return my_list
        elif len(my_list) == 2:
            return my_list if my_list[0] <= my_list[1] else my_list[::-1]
        else:
            return merge(div_half(my_list[:len(my_list) // 2]),
                         div_half(my_list[len(my_list) // 2:]))

    return div_half(my_list)


IN_LIST = [uniform(0.0, 50.0) for i in range(10)]

print(IN_LIST)
print(merge_sort(IN_LIST))

# Результат
# [40.66832066377046, 41.32023034368247, 45.18854582044614, 24.167202416647914 ....]
# [1.6039689261568513, 8.913995798006274, 9.312809770630636, 10.449208819206568 ....]

