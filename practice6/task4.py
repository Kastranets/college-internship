import random
from math import sqrt


nested_list = []
for _ in range(10):
    sublist = []
    for _ in range(3):
        num = round(random.uniform(0, 10), 1)
        sublist.append(num)
    nested_list.append(sublist)

for i in nested_list:
    a, b, x = i[0], i[1], i[2]
    if a > b and x >= 2:
        print(f"числа: a = {a}, b = {b}, x = {x}:     sqrt(a + b) - 1.5 * b * x = {sqrt(a + b) - 1.5 * b * x}")
    else:
        print(f"числа: a = {a}, b = {b}, x = {x}:     a ** 2 + 2 * (a + sqrt(b) = {a ** 2 + 2 * (a + sqrt(b))}")