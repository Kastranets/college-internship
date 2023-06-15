from math import sin, cos, sqrt


x = 1.8
a = x + 3
y = 0.35 * a

if x <= 0:
    result = x ** 2 - sin(y)
else:
    result = sqrt(x) + cos(y)

print(result)