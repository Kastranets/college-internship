N = input("Яку суму грошей ви маєте N = ")
first_product = input("Введіть ціну першого товару: ")
second_product = input("Введіть ціну другого товару: ")
third_product = input("Введіть ціну третього товару: ")

if first_product + second_product + third_product > N:
    print("Недостатньо грошей на рахунку")
else:
    print("Товари оплачено")