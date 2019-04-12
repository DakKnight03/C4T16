number = input("enter your age: ")
if int(number) >= 18:
    print("you can watch this movie")
else:
    print("you cant watch this movie")
if int(number) >= 18:
    date = input("when would you like to watch the movie? ")
    if int(date) > 24:
        print("date chosen is not valid")
    else:
        print("nice choice! We'll meet you at %spm!" % int(date))


