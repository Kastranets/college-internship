n = [10, 50, 100]
x = 0.69

for i in n:
    sum = 0
    for k in range(0, i+1):
        sum += (pow(-1, k) * pow(x, k)) / pow(k + 1, 2)
    print(f"Сума перший {i} членів ряду ((-1)^(k + 1) * x^k) / (k + 1)^2 = {sum}")