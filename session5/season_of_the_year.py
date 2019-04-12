month = int(input("enter a month: "))

if month <= 12:
    if month <= 3:
        print("it is spring")
    elif 3 < month <= 6:
        print("it is summer")
    elif 6 < month <= 9:
        print("it is autumn")
    else:
        print("it is winter")
else:
    print("please enter a valid month")