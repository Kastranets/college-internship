def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i <= int(number ** 0.5):
        if number % i == 0:
            return False
        i += 1
    return True

def frac_by_N(N, A, B):
    i = A
    while i <= B:
        if i % (N + 3) == 0:
            return i
        i += 1
    else:
        return False

i = 6
while i <= 10:
    if is_prime(i):
        print(f"Число {i} є простим")
    else:
        print(f"Число {i} не є простим")
    i += 1

while True:
    try:
        A, B = map(int, input("Введіть два числа: ").split())
        result = frac_by_N(16, A, B)
        if not result:
            print("Немає дільників")
        else:
            print(f"Першим числом з проміжку [{A}, {B}]"
                  f" яке ділиться на {16+3} є {result}")
    except:
        print("Ви ввели не числа")
