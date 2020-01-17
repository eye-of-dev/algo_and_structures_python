"""
#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
"""

from random import randint

IN_LIST = [randint(-30, 30) for i in range(30)]

MIN_EL = -30
MIN_EL_KEY = 0
MIN_EL
for key, value in enumerate(IN_LIST):
    # поиск минимального элемента и его индекса
    if 0 > value > MIN_EL:
        MIN_EL = value
        MIN_EL_KEY = key

    # при случае, MIN_EL минимально возможному - прекращаем поиск
    # if MIN_EL == -30:
    #     break

print(f'Исходный массив {IN_LIST}')

if MIN_EL >= 0:
    print('В массиве нет отрицательных элементов')
else:
    print(f'Минимальный отрицательный элемент в массве {MIN_EL} и его индекс {MIN_EL_KEY}')
