from math import factorial, log
N = int(input("Введіть число N яке буде більшим за 10: "))
x = int(input("Введіть число x: "))

sum = 0
for i in range(N+1):
    sum += pow(-1, i) * pow(log(3), i) / factorial(i) * pow(x, i)

print(f"При x = {x} значення суми ((-1)^i * ln^i(3)) / i! * x^i де і від 0 до {N} = {sum}")