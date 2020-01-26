"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# OC - Ubuntu 18.04 x64
# Python 3.6


from memory_profiler import profile


@profile
def multiple_ranges():
    """
    В диапазоне натуральных чисел от 2 до 99 определить,
    сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
    """

    for i in range(2, 9):
        a_arr = [j for j in range(2, 99) if j % i == 0]
        len_arr = len(a_arr)
        print('Колличество кратных %d элементов в диапазоне от 2 до 99 равно %d' % (i, len_arr))


# Line #    Mem usage    Increment   Line Contents
# ================================================
#    18     14.2 MiB     14.2 MiB   @profile
#    19                             def multiple_ranges():
#    20                                 """
#    21                                 В диапазоне натуральных чисел от 2 до 99 определить,
#    22                                 сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
#    23                                 """
#    24
#    25     14.2 MiB      0.0 MiB       for i in range(2, 9):
#    26     14.2 MiB      0.0 MiB           a_arr = [j for j in range(2, 99) if j % i == 0]
#    27     14.2 MiB      0.0 MiB           print('Колличество кратных %d элементов
#                                           в диапазоне от 2 до 99 равно %d' % (i, len(a_arr)))

@profile
def search_prime(numb):
    """
    нахождения i-го по счёту простого числа
    :param numb: Порядковый номер простого числа
    :return: Возвращает число
    """
    count, number, prime = 1, 1, [2]

    if numb == 1:
        return 2

    while count != numb:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number


# Line #    Mem usage    Increment   Line Contents
# ================================================
#    47     14.2 MiB     14.2 MiB   @profile
#    48                             def search_prime(numb):
#    49                                 """
#    50                                 нахождения i-го по счёту простого числа
#    51                                 :param numb: Порядковый номер простого числа
#    52                                 :return: Возвращает число
#    53                                 """
#    54     14.2 MiB      0.0 MiB       count, number, prime = 1, 1, [2]
#    55
#    56     14.2 MiB      0.0 MiB       if numb == 1:
#    57                                     return 2
#    58
#    59     14.2 MiB      0.0 MiB       while count != numb:
#    60     14.2 MiB      0.0 MiB           number += 2
#    61
#    62     14.2 MiB      0.0 MiB           for num in prime:
#    63     14.2 MiB      0.0 MiB               if number % num == 0:
#    64     14.2 MiB      0.0 MiB                   break
#    65                                     else:
#    66     14.2 MiB      0.0 MiB               count += 1
#    67     14.2 MiB      0.0 MiB               prime.append(number)
#    68
#    69     14.2 MiB      0.0 MiB       return number


@profile
def eratosthenes_sieve(numb):
    """
    нахождения i-го по счёту простого числа
    :param numb: Порядковый номер простого числа
    :return: Возвращает число
    """
    count, start, end = 1, 3, 4 * numb

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if numb == 1:
        return 2

    while count < numb:
        for i in range(len(sieve)):
            if sieve[i] != 0:
                count += 1

                if count == numb:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * numb
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):
            for num in prime:
                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break


# Line #    Mem usage    Increment   Line Contents
# ================================================
#   102     14.2 MiB     14.2 MiB   @profile
#   103                             def eratosthenes_sieve(numb):
#   104                                 """
#   105                                 нахождения i-го по счёту простого числа
#   106                                 :param numb: Порядковый номер простого числа
#   107                                 :return: Возвращает число
#   108                                 """
#   109     14.2 MiB      0.0 MiB       count, start, end = 1, 3, 4 * numb
#   110
#   111     14.2 MiB      0.0 MiB       sieve = [i for i in range(start, end) if i % 2 != 0]
#   112     14.2 MiB      0.0 MiB       prime = [2]
#   113
#   114     14.2 MiB      0.0 MiB       if numb == 1:
#   115                                     return 2
#   116
#   117     14.2 MiB      0.0 MiB       while count < numb:
#   118     14.2 MiB      0.0 MiB           for i in range(len(sieve)):
#   119     14.2 MiB      0.0 MiB               if sieve[i] != 0:
#   120     14.2 MiB      0.0 MiB                   count += 1
#   121
#   122     14.2 MiB      0.0 MiB                   if count == numb:
#   123     14.2 MiB      0.0 MiB                       return sieve[i]
#   124
#   125     14.2 MiB      0.0 MiB                   j = i + sieve[i]
#   126
#   127     14.2 MiB      0.0 MiB                   while j < len(sieve):
#   128     14.2 MiB      0.0 MiB                       sieve[j] = 0
#   129     14.2 MiB      0.0 MiB                       j += sieve[i]
#   130
#   131     14.2 MiB      0.0 MiB           prime.extend([i for i in sieve if i != 0])
#   132
#   133     14.2 MiB      0.0 MiB           start, end = end, end + 2 * numb
#   134     14.2 MiB      0.0 MiB           sieve = [i for i in range(start, end) if i % 2 != 0]
#   135
#   136     14.2 MiB      0.0 MiB           for i in range(len(sieve)):
#   137     14.2 MiB      0.0 MiB               for num in prime:
#   138     14.2 MiB      0.0 MiB                   if sieve[i] % num == 0:
#   139     14.2 MiB      0.0 MiB                       sieve[i] = 0
#   140     14.2 MiB      0.0 MiB                       break

@profile
def symbols(i, end):
    """ Выводим символы по парно
    :param i: коды таблицы ASCII
    :param end: счетчик
    :return: "код-символ"
    """
    if i <= 185:
        if (end % 10) == 0:
            print(i, chr(i), sep=' - ')
            end = 1
        else:
            print(i, chr(i), sep=' - ', end=' ')
        return symbols(i + 1, end + 1)


# Line #    Mem usage    Increment   Line Contents
# ================================================
#   180     15.6 MiB     15.4 MiB   @profile
#   181                             def symbols(i, end):
#   182                                 """ Выводим символы по парно
#   183                                 :param i: коды таблицы ASCII
#   184                                 :param end: счетчик
#   185                                 :return: "код-символ"
#   186                                 """
#   187     15.6 MiB      0.3 MiB       if i <= 185:
#   188     15.6 MiB      0.0 MiB           if (end % 10) == 0:
#   189     15.6 MiB      0.0 MiB               print(i, chr(i), sep=' - ')
#   190     15.6 MiB      0.0 MiB               end = 1
#   191                                     else:
#   192     15.6 MiB      0.0 MiB               print(i, chr(i), sep=' - ', end=' ')
#   193     15.6 MiB      0.0 MiB           return symbols(i + 1, end + 1)

# Не стал все копировать. Скопировал часть вывода, чтобы было видно Increment
# данный вывод показвает, что изначально выделенной пямяти не хватило


if __name__ == '__main__':
    multiple_ranges()
    search_prime(50)
    eratosthenes_sieve(50)
    symbols(32, 1)
