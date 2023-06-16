import math as m1

x = float(input('Введіть значення x: '))

try:
    y = m1.sin(x)**2 - ((m1.sqrt(m1.log10(abs(2-x))) + m1.log10(x)) / (3 * m1.sqrt(m1.tan(x)) + m1.sqrt(m1.cos(x)**3)))
    print(y)
except ValueError:
    print("Значення в цій точці не існує")