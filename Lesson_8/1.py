"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

# Дисклеймер
# не претендую на авторство данного кода, т.к. найден на просторах интернета.
#
#
#
# Для себя: теперь я знаю что такое алгоритм Хаффмана, могу им пользоваться
# и самое главное где и когда его можно использовать


import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    """
    Кодируем струку
    :param s: Входная строка
    :return: Закодированная строка
    """
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(encoded, code):
    """
    Декодируем строку
    :param encoded: Исходный набор символов
    :param code: Закодированная строка
    :return: Раскодированная строка
    """
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)


MY_STR = 'veni vidi vici'
CODE = huffman_encode(MY_STR)
ENCODE = "".join(CODE[ch] for ch in MY_STR)
MY_STR = huffman_decode(ENCODE, CODE)
print(CODE)
print(MY_STR)
MY_STR = 'beep boop beer'
CODE = huffman_encode(MY_STR)
ENCODE = "".join(CODE[ch] for ch in MY_STR)
MY_STR = huffman_decode(ENCODE, CODE)
print(CODE)
print(MY_STR)

# результат
# {'d': '000', 'c': '001', 'v': '01', ' ': '100', 'e': '1010', 'n': '1011', 'i': '11'}
# veni vidi vici
# {'b': '00', 'r': '010', 'p': '011', 'e': '10', ' ': '110', 'o': '111'}
# beep boop beer
