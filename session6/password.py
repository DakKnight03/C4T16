while True:
    password = input("enter your password: ")

    if len(password) >= 8:
        if password.isalpha() == False:
            print("done.")
            break
        else:
            print("password must have numbers.")
    else:
        print("password must have 8 or more characters.")

