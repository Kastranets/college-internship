print("Переведення миль в кілометри:")
for miles in range(100, 1100, 100):
    kilometers = miles * 1.609344
    print(f"{miles} миль = {kilometers} км")

print()

print("Переведення кілометрів в милі:")
for kilometers in range(100, 1100, 100):
    miles = kilometers / 1.609344
    print(f"{kilometers} км = {miles} миль")
