def boolean_function(x, y, z):
    return int((not (z * x)) or (x * (not y)) or (x * y * (not z)))

print("x | y | z | f(x, y, z)")
print("---------------------")

for x in range(2):
    for y in range(2):
        for z in range(2):
            result = boolean_function(x, y, z)
            print(f"{x} | {y} | {z} | {result}")