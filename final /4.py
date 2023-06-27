A = (3.1, -7.8, 6.2, -3.3, 1.1)
res = 1

for i in A:
    if i > -5.4:
        res *= i
        print(f"{i}", end=" * ")
print(f'1 = {res}')