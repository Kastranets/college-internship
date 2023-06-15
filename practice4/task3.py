from math import sin, pi, sqrt

print("Обрахування значення функції y = (sin(pi / 2) / b) * sqrt(m)\n")
while True:
    b, m = input("Введіть значення b: "), input("Введіть значення m (воно повинно бути невід'ємним): ")
    try:
        b, m = float(b), float(m)
        print(sqrt(m) * sin(pi / 2)  / 6)
    except ValueError:
        print("Ви ввели некоретні значення")