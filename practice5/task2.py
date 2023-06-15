for x in range(2):
    print(f"№9 Закон нуля і oдиниці -- x * (not x) = 0, при х = {x} значення {x * (not x)}")

print('')
for x in range (2):
    print(f"№9 Закон нуля і oдиниці -- x and 1 = x, при х = {x} значення {x and 1}")

print('')
for x in range(2):
    print(f"№10 3акон нуля і oдиниці -- x or (not x) = 1, при х = {x}, значення {x or (not x)}")

print('')
for x in range(2):
    print(f"№10 3акон нуля і oдиниці -- x or 0 = x при х = {x}, значення {x or 0}")

print('')
for x in range(2):
    for y in range(2):
        print(f"№15 Закон склеювання -- (x or (not y)) and (x or y) = x, при x {x}, y {y} має значення "
              f"{int((x or (not y)) and (x or y))}")

print('')
for x in range(2):
    for y in range(2):
        print(f"№16 Закон склеювання -- (x and (not y)) and (x and y) = x, при x {x}, y {y} має значення "
              f"{int((x and (not y)) and (x and y))}")

print('')
for x in range(2):
    for y in range(2):
        print(f"#13 закон Де Моргана -- not(x and y) = (not x) or (not y), при x {x}, y {y}: "
              f"{int(not(x and y))} = {int((not x) or (not y))}")

