while True:
    N = int(input("Введіть вартість покупки: "))

    if N < 1000:
        print("Знижки немає")
    elif N < 2000:
        print("Знижка 2%")
    elif N < 5000:
        print("Знижка 5%")
    else:
        print("Знижка 10%")
