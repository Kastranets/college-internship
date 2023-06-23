numbers = [64, 649, 351, 8376771905, 67044, 55004329]

i = 0
for number in numbers:
    count = 1
    while number >= 10:
        number //= 10
        count += 1

    print(f"Кількість цифр у числі {numbers[i]} = {count}")
    i += 1

