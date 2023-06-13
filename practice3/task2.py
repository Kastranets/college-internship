from math import tan, atan, cos, pi, exp, sin


x = 1

result_first = 2 * atan(3) + 2 * tan(pi / 9) - 5 * cos(4.2 * x)
result_second = 3 / 8 * x ** 3 + 2 * cos(pi / 16) + 4 * exp(sin(2 * x))

print(f"Вираз 16 2arctg3 + tg(pi/9) – 5cos4,2 {result_first}, \nВираз 3/8x3+ 2cos(pi/16) + 4e^sin2x {result_second} \nпри x = {x}")