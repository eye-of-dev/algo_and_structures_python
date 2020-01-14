"""
# 4.	Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

IN_LIST = [randint(0, 30) for i in range(30)]

# c словарем было бы легче:D
# в качестве ключа значение из массиа,
# а в качестве значения кол-во повторений

print(f'Исходный список {IN_LIST}')

NUM = IN_LIST[0]
MAX_REP = 1
for i in range(30 - 1):
    count = 1
    for k in range(i + 1, 30):
        if IN_LIST[i] == IN_LIST[k]:
            count += 1
    if count > MAX_REP:
        MAX_REP = count
        NUM = IN_LIST[i]

if MAX_REP > 1:
    print(f'{MAX_REP} раз(а) встречается число {NUM}')
else:
    print('Все элементы уникальны')
