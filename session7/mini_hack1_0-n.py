n = int(input("choose a number: "))
if n > 0:
    if n % 2 == 0:
        print("n must be an odd number.")
    else:
        for i in range(n, 0, -2):
            print(i, end = " ")
else:
    print("n must be bigger than 0.")