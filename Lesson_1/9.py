"""
# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).
"""
NUMB_A = int(input('Первое число: '))
NUMB_B = int(input('Второе число: '))
NUMB_C = int(input('Третье число: '))

if NUMB_B < NUMB_A < NUMB_C or NUMB_C < NUMB_A < NUMB_B:
    print('Среднее:', NUMB_A)
elif NUMB_A < NUMB_B < NUMB_C or NUMB_C < NUMB_B < NUMB_A:
    print('Среднее:', NUMB_B)
else:
    print('Среднее:', NUMB_C)
