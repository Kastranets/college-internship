from math import sqrt


print("Програма для обчислення значення виразу в залежності від введеного а, та b = номер варіанта (16)\n"
      "(17.1 * (3.8 * a + sqrt(5 * b))) / (3 - b) за умови, що a > 0 and b > 1\n"
      "sqrt(7.5 * sqrt (pow(a, 3) + 2.3 * a)) за умови, що a > 0 and b <= 1\n"
      "26.3 * (2.4 * a ** 3 + 2.3 * a) за умови, що a <= 0\n")

while True:
    a = input("Введіть а: ")
    b = 16

    try:
        a = float(a)
        if a > 0 and b > 1:
            y = (17.1 * (3.8 * a + sqrt(5 * b))) / (3 - b)
            print(f"Значення функції (17.1 * (3.8 * a + sqrt(5 * b))) / (3 - b) в точці ({a}, {b}) = {y}")
        elif a > 0 and b <= 1:
            y = sqrt(7.5 * sqrt (pow(a, 3) + 2.3 * a))
            print(f"Значення функції sqrt(7.5 * sqrt (pow(a, 3) + 2.3 * a)) в точці ({a}, {b}) = {y}")
        elif a <= 0:
            y = 26.3 * (2.4 * a ** 3 + 2.3 * a)
            print(f"Значення функції 26.3 * (2.4 * a ** 3 + 2.3 * a в точці ({a}, {b}) = {y}")
    except ValueError:
        print("Ви ввели не число")


