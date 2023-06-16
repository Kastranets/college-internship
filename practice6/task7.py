def maximum(x, y):
    return x if x > y else y

def minimum(x, y):
    return x if x < y else y
def maxmin(x, y):
    return [maximum(x, y), minimum(x, y)]

def min_of_3(x, y, z):
    return minimum(x, minimum(y, z))

def max_of_3(x, y, z):
    return maximum(x, maximum(y, x))

def find_middle_number(x, y, z):
    if x <= y <= z or z <= y <= x:
        middle = y
    elif y <= x <= z or z <= x <= y:
        middle = x
    else:
        middle = z

    return middle

x, y, z = input("Введіть х: "), input("Введіть y: "), input("Введіть z: ")
try:
    x, y, z = float(x), float(y), float(z)
    print(f"\nМаксимальне значення серед перших двох чисел ({x}, {y}): {maximum(x, y)}")
    print("Максимальне значення серед перших двох чисел ({}, {}): {}, а мінімальне: {}".format(x, y, *maxmin(x, y)))
    print(f"Мінімальне значення з трьох чисел ({x}, {y}, {z}) -- {min_of_3(x, y, z)}")
    print(f"Максимальне значення з трьох чисел ({x}, {y}, {z}) -- {max_of_3(x, y, z)}")
    print(f"Медіана з трьох чисел ({x}, {y}, {z}) -- {find_middle_number(x, y, z)}")
except:
    print("Ви ввели не число")