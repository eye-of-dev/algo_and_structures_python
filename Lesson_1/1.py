"""
# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

NUMB = int(input('Введите трехзначное число: '))
NUM_ONE = NUMB // 100
NUM_TWO = NUMB % 100 // 10
NUM_THREE = NUMB % 10

print("Сумма цифр введеного числа: ", NUM_ONE + NUM_TWO + NUM_THREE)
print("Произведение цифр введеного числа: ", NUM_ONE * NUM_TWO * NUM_THREE)
