"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

# OC - Ubuntu 18.04 x64
# Python 3.6
# Выводы из данной работы:
# Если предполагается, что в класс/объект не будут добавлять
# атрибуты, то лучше использовать класс с применением слотов,
# т.е. ресурсов под это выделяется значительно меньше

from pympler import asizeof


class BasicClass:
    def __init__(self, param_x, param_y):
        self.param_x = param_x
        self.param_y = param_y


BC_OBJ = BasicClass(5, 6)
BC_OBJ.param_z = 7
print(BC_OBJ.__dict__)
print(asizeof.asizeof(BC_OBJ))


class SlotsClass:
    __slots__ = ('param_x', 'param_y', 'param_z')

    def __init__(self, param_x, param_y):
        self.param_x = param_x
        self.param_y = param_y


SC_OBJ = SlotsClass(5, 6)
BC_OBJ.param_z = 7
print(SC_OBJ.__slots__)
print(asizeof.asizeof(SC_OBJ))

# BasicClass
# {'param_x': 5, 'param_y': 6, 'param_z': 7}
# 432

# SlotsClass
# ('param_x', 'param_y', 'param_z')
# 128#
#
