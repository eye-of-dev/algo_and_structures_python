"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

from timeit import Timer


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


t1 = Timer("search_prime(5)", setup="from __main__ import search_prime")
print('search_prime', t1.timeit(number=1000), 'milliseconds')


# Сложность близка к O(n**2)
# timeit выдает результат 0.00243547599984594

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


t1 = Timer("eratosthenes_sieve(5)", setup="from __main__ import eratosthenes_sieve")
print('eratosthenes_sieve', t1.timeit(number=1000), 'milliseconds')

# Сложность близка к O(n**3)
# timeit выдает результат 0.005870107000191638


# ВЫВОД:
# Реализация нахождения i-го числа без решета Эротосфера
# выглядит и эстетичнее и по производительности выигрывает.
# Либо 3-й вариант - голова у меня не из того места растет :D
