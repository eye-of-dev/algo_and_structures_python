"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

NUMB_ONE = int(input("Количество вводимых чисел? "))
NUMB_TWO = int(input("Цифра, которую необходимо посчитать: "))
COUNT = 0
for i in range(1, NUMB_ONE + 1):
    m = int(input("Введите число " + str(i) + ": "))
    while m > 0:
        if m % 10 == NUMB_TWO:
            COUNT += 1
        m = m // 10

print("Было введено %d цифр %d" % (COUNT, NUMB_TWO))
