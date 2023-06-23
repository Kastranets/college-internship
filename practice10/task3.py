k = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a + b + c == a * b * c:
                print(100 * a + 10 * b + c)
                k += 1

print(f"k = {k}")