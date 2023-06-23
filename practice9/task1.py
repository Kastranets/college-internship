i = 0
while i < 10:
    print("i =", i)
    i += 1
print("\n")

i = 5
while i < 10:
    print("i =", i)
    i += 1
print("\n")

i = 5
while i < 10:
    print("i =", i)
    i += 2
print("\n")

i = 0
while i < 3:
    response = input("Введіть stop, щоб зупинити цикл (інакше що завгодно): ")
    if response == "stop":
        break
    i += 1
else:
    print("Цикл сам був завершений")
