from math import sqrt

a = float(input("Уведіть число а: "))
b = float(input("Уведіть число b: "))
x = 16

if x > b and x >= 2:
    y = sqrt(a + b) - 1.5 * b * x
else:
    y = pow(a, 2) + 2 * (a + sqrt(b))

print(f"y = {y}")