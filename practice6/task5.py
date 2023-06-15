x = 16

while True:
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    try:
        a, b, c = float(a), float(b), float(c)
        if x > 0:
            print(f"a ** 2 - b * x = {a ** 2 - b * x}")
        else:
            print(f"a ** 2 - (c + x / b) = {a ** 2 - (c + x / b)}\n") #LOL
    except ValueError:
        print("Ви ввели не число, спробуйте че раз")