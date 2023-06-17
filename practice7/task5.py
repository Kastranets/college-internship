while True:
    score = input("Enter your result: ")

    try:
        score = int(score)
        if score < 0 or score > 100:
            print("You entered an incorrect number of points")
            break
        else:
            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "F"

        print(f"Grade is {grade}")
    except ValueError:
        print("You have not entered a number")
