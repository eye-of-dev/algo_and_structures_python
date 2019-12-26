"""
# 3. По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.
"""
print("Введите координаты первой точки (x1;y1):")
X_ONE = float(input("X1 = "))
Y_ONE = float(input("Y1 = "))

print("Введите координаты второй точки(x2;y2):")
X_TWO = float(input("X2 = "))
Y_TWO = float(input("Y2 = "))

print("Уравнение прямой, проходящей через эти точки:")
NUMB_K = (Y_ONE - Y_TWO) / (X_ONE - X_TWO)
NUMB_B = Y_TWO - NUMB_K * X_TWO
print("y = %.2f*x + %.2f" % (NUMB_K, NUMB_B))
