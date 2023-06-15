from math import exp, tan, cos, sqrt


print("Обрахування значення функції y = (exp(-3 * x) + tan(4 * x - 1)) / (abs(cos(x)) + sqrt(cos((2 * x)))))\n")
while True:
    x = input("Введіть значення х: ")
    try:
        x = float(x)
        y = (exp(-3 * x) + tan(4 * x - 1)) / (abs(cos(x)) + sqrt(cos((2 * x))))
        print(y)
    except ValueError:
        print("Ви ввели не число ")