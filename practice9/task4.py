n = [10, 50, 100]
x = 0.69

for i in n:
    k = 0
    sum = 0
    while k <= i:
        sum += (pow(-1, k) * pow(x, k)) / pow(k + 1, 2)
        k += 1
    print(f"Сума перших {i} членів ряду ((-1)^(k + 1) * x^k) / (k + 1)^2 = {sum}")
