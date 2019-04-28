
from random import randint
while True:
    a = randint(-20, 20)
    b = randint(-20, 20)
    c = randint(-1, 1)
    true = "true"
    false = "false"
    math = a + b + c
    print(a, "+", b, "=", math)
    answer = input("true or false? ")
    if c == 0:
        if answer == true:
            print("correct")
        elif answer == false:
            print("incorrect")
        else:
            print("enter true or false")
    else:
        if answer == true:
            print("incorrect")
        elif answer == false:
            print("correct")
        else:
            print("enter true or false")

