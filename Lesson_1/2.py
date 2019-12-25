"""
# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

NUMB_FIVE = 5
NUMB_SIX = 6

print("%d & %d = %d (%s)" % (NUMB_FIVE, NUMB_SIX, NUMB_FIVE & NUMB_SIX,
                             bin(NUMB_FIVE & NUMB_SIX)))
print("%d | %d = %d (%s)" % (NUMB_FIVE, NUMB_SIX, NUMB_FIVE | NUMB_SIX,
                             bin(NUMB_FIVE | NUMB_SIX)))
print("%d ^ %d = %d (%s)" % (NUMB_FIVE, NUMB_SIX, NUMB_FIVE ^ NUMB_SIX,
                             bin(NUMB_FIVE ^ NUMB_SIX)))

print("%d << 2 = %d (%s)" % (NUMB_FIVE, NUMB_FIVE << 2, bin(NUMB_FIVE << 2)))
print("%d >> 2 = %d (%s)" % (NUMB_FIVE, NUMB_FIVE >> 2, bin(NUMB_FIVE >> 2)))
