while True:
    username = input("enter username: ")
    password = input("enter password: ")
    email = input("enter email: ")
    if len(password) > 8 and ("@") in email and (".com") in email:
        print(username)
        print(password)
        print(email)
        re_enter_password = input("re-enter your password: ")
        if re_enter_password != password:
            print("incorrect")
        else:
            print("done")
            break
    else:
        print("invalid")