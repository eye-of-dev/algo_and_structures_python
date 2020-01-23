"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

Enterprise = namedtuple('Enterprise', 'name quarter_1 quarter_2 quarter_3 quarter_4 year')

ENTERPRISE_COUNT = int(input('Введите количество предприятий для анализа: '))
ENTERPRISES = [0 for _ in range(ENTERPRISE_COUNT)]
PROFIT_SUM = 0

for i in range(ENTERPRISE_COUNT):
    name = input(f'Введите название {i + 1}-го предприятия: ')
    quarters = [float(j) for j in input('Введите через пробел '
                                        'прибыль в каждом квартале: ').split()]

    year = 0
    for quarter in quarters:
        year += quarter

    PROFIT_SUM += year
    ENTERPRISES[i] = Enterprise(name, *quarters, year)

if ENTERPRISE_COUNT == 1:
    print(f'Для анализа передано 1 предприятие: {ENTERPRISES[0].name}. '
          f'Eго годовая прибыль: {ENTERPRISES[0].year}')

else:
    PROFIT_AVERAGE = PROFIT_SUM / ENTERPRISE_COUNT

    LESS = []
    MORE = []

    for i in range(ENTERPRISE_COUNT):

        if ENTERPRISES[i].year < PROFIT_AVERAGE:
            LESS.append(ENTERPRISES[i])

        elif ENTERPRISES[i].year > PROFIT_AVERAGE:
            MORE.append(ENTERPRISES[i])

    print(f'\nСредняя годовая прибыль по предприятиям: {PROFIT_AVERAGE: .2f}')

    print(f'Предприятия, чья прибыль меньше {PROFIT_AVERAGE: .2f}:')
    for ent in LESS:
        print(f'Предприятие "{ent.name}" с прибылью {ent.year: .2f}')

    print(f'\nПредприятия, чья прибыль больше {PROFIT_AVERAGE: .2f}:')
    for ent in MORE:
        print(f'Предприятие "{ent.name}" с прибылью {ent.year: .2f}')
