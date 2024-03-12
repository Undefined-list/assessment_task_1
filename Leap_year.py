try:
    year = int(input("What year do you want to tell if its a leap year? "))
except:
    print("What you enter must be a number.")
else:
    isitleap = year % 4
    notleap = year % 100
    yesleap = year % 400
    if notleap == 0 or isitleap != 0:
        if yesleap == 0:
            print(f"{year} is a leap year")
        else:
             print(f"{year} is not a leap year")
    if notleap != 0:
        if isitleap == 0:
            print(f"{year} is a leap year")