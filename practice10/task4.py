N = 8
print("Прості числа")
while (N < 50):
    diln = 2
    while (diln <= (N / diln)):
        if not (N % diln):
            break
        diln += 1
    if (diln > N / diln):
        print(N, end=" ")
    N += 1
