"""
#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
"""

from random import randint
from random import shuffle

IN_LIST = list(set(randint(0, 30) for i in range(30)))
# определим переменные, минимальному зададим максимальное значение,
# а максимальному минимальное
MIN_EL = 30
MAX_EL = 0
MIN_EL_KEY = 0
MAX_EL_KEY = 0

# перемешаем "массив", чтобы было интереснее
shuffle(IN_LIST)
for key, value in enumerate(IN_LIST):

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

print(f'Исходный массив {IN_LIST}')
# переставляем местами минимальное и максимальное значение
IN_LIST[MIN_EL_KEY], IN_LIST[MAX_EL_KEY] = IN_LIST[MAX_EL_KEY], IN_LIST[MIN_EL_KEY]

print(f'В списке минимальное и максимальное переставлены местами {IN_LIST}')
