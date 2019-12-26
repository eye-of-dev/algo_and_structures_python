"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

SIDE_ONE = int(input("Введите длину первой стороны "))
SIDE_TWO = int(input("Введите длину второй стороны "))
SIDE_THREE = int(input("Введите длину третьей стороны "))

if (SIDE_ONE + SIDE_TWO) > SIDE_THREE and (SIDE_ONE + SIDE_THREE) > SIDE_TWO and (SIDE_TWO + SIDE_THREE) > SIDE_ONE:
    if SIDE_ONE != SIDE_TWO and SIDE_ONE != SIDE_THREE and SIDE_TWO != SIDE_THREE:
        print('Этот треугольник разносторонний')
    elif SIDE_ONE == SIDE_TWO and SIDE_ONE == SIDE_THREE:
        print('Этот треугольник равносторонний')
    else:
        print('Этот треугольник равнобедренный')
else:
    print('Это не треугольник')
