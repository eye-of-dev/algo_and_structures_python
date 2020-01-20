"""
# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import random

NUMB = 10
ROWS = 5
RESULT_MATR = []
for i in range(ROWS):
    b = []
    for j in range(NUMB):
        n = int(random() * 100)
        b.append(n)
        print('%4d' % n, end='')
    RESULT_MATR.append(b)
    print()

MAX_EL = -1
for j in range(NUMB):
    min_el = 200
    for i in range(ROWS):
        if RESULT_MATR[i][j] < min_el:
            min_el = RESULT_MATR[i][j]
    if min_el > MAX_EL:
        MAX_EL = min_el

print("Максимальный среди минимальных: ", MAX_EL)
