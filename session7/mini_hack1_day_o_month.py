month = int(input("choose a month: "))
if 0 < month < 13:
    if month in (1, 3, 5, 7, 8, 10, 12):
        print("there are 31 days in this month")
    elif month in (4, 6, 9, 11):
        print("there are 30 days in this month")
    else:
        print("there are 28 days in this month")
else:
    print("enter a valid month")