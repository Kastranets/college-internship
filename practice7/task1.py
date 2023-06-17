while True:
    N = int(input("Яку суму грошей ви маєте N = "))
    first_product = int(input("Введіть ціну першого товару: "))
    second_product = int(input("Введіть ціну другого товару: "))
    third_product = int(input("Введіть ціну третього товару: "))

    if first_product + second_product + third_product > N:
        print("Недостатньо грошей на рахунку")
    else:
        print("Товари оплачено")