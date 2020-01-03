"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

NUMB = int(input('Введите количество элементов: '))
NUMB_ONE = 1
NUMB_TWO = 0
for i in range(NUMB):
    NUMB_TWO += NUMB_ONE
    NUMB_ONE /= -2
print(NUMB_TWO)
