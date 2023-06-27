from math import cos
while True:
    x = int(input('Введіть х: '))
    a = int(input('Введіть a: '))

    if x >= 0 and x <= 2:
        y = (pow(cos(pow(x * a, 3)), 2))/(pow(a, 1 / 6))
        print(f'При a = {a} та при x = {x} вираз cos^2(xa)^3 / a^(1/6) = {y}')
    if x < 0 or x >= 3:
        y = x**2 - a*x
        print(f'При a = {a} та при x = {x} вираз x^2 - ax= {y}')

