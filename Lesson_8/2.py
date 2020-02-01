"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

from hashlib import sha1

MY_STR = input('Введите строку: ')

STR_LEN = len(MY_STR)
SUB_LEN = 1

SUB_STRS = []

while STR_LEN > 1:
    for i in range(STR_LEN):
        sub = sha1(MY_STR[i:i + SUB_LEN].encode('utf-8')).hexdigest()
        if sub not in SUB_STRS:
            SUB_STRS.append(sub)
    SUB_LEN += 1
    STR_LEN -= 1

print(f'В строке "{MY_STR}" {len(SUB_STRS)} уникальных подстрок')
