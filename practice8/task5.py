def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def frac_by_N(N, A, B):
    for i in range(A, B + 1):
        if i % (N + 3) == 0:
            return i
    else:
        return False

for i in range(6, 10):
    print(f"Число {i} є простим") if is_prime(i) else print(f"Число {i} не є простим")

while True:
    try:
        A, B = map(int, input("Введіть два числа: ").split())
        result = frac_by_N(16, A, B)
        print("Немає дільників") if (not result) else print(f"Першим числом з проміжку [{A}, {B}] яке ділиться на {16+3} є {result}")
    except:
        print("Ви ввели не числа")