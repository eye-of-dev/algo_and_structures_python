"""
# 8. Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
# Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.
"""

YEAR = int(input("Введите год: "))

if YEAR % 4 != 0 or (YEAR % 100 == 0 and YEAR % 400 != 0):
    print("Не високосный")
else:
    print("Високосный")
