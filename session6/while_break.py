
while True:
    name = input("what is your name? ")
    if name.isdigit():
        print("not a name")
    else:
        print("so your name is", name)
        break

