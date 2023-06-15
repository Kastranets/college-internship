from math import sin, cos


print("Обрахування значення функції y = sin(x) - cos(x ** 3) * sin(x ** 2 -4.2) + 4.27\n")
while True:
    x = input("Введіть значення х: ")
    try:
        x = float(x)
        y = sin(x) - cos(x ** 3) * sin(x ** 2 - 4.2) + 4.27
        print(y)
    except ValueError:
        print("Ви ввели не число ")