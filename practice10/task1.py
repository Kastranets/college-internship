while True:
    N = int(input())
    f1 = 1
    f2 = 1
    while N > f2:
        f = f2
        f2 += f1
        f1 = f
    if N == f2:
        print("True")
    else:
        print("False")