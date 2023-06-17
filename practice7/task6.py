while True:
    try:
        month = int(input("Введіть номер місяця: "))

        if month == 1 or month == 2 or month == 12:
            season = "Зима"
        elif month >= 3 and month <= 5:
            season = "Весна"
        elif month >= 6 and month <= 8:
            season = "Літо"
        elif month >= 9 and month <= 11:
            season = "Осінь"
        else:
            season = "Невідомий місяць"

        print(f"Пора року - {season}")

    except ValueError:
        print("Ви ввели не число")