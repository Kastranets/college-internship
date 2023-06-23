print("Переведення миль в кілометри:")
miles = 100
while miles <= 1000:
    kilometers = miles * 1.609344
    print(f"{miles} миль = {kilometers} км")
    miles += 100

print()

print("Переведення кілометрів в милі:")
kilometers = 100
while kilometers <= 1000:
    miles = kilometers / 1.609344
    print(f"{kilometers} км = {miles} миль")
    kilometers += 100
