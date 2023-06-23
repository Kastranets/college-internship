P = float(input("Введіть відсоткову ставку (P): "))
deposit = 1000
month = 0

while month < 36:
    deposit += deposit * (P / 100)
    month += 1
    if deposit > 1100:
        break

print(f"Вклад перевищить 1100 грн після {month} місяців")
print(f"Остаточна сума вкладу становитиме {deposit:.2f} грн")
