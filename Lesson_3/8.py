"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

NUMB = 5
ROWS = 4
RESULT_MATR = []
for i in range(ROWS):
    b = []
    s = 0
    print("%d-я строка:" % (i + 1))
    for j in range(NUMB - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    RESULT_MATR.append(b)

for i in RESULT_MATR:
    print(i)
