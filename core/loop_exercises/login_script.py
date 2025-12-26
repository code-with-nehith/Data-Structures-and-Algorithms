def login_system():
    secret_password = "nehith reddy"
    attempts = 3

    while attempts > 0:
        password = input("Enter password: ")

        if password == secret_password:
            print("Welcome!")
            return
        else:
            attempts -= 1
            print("Access Denied")

    print("Account Locked.")
  

login_system()