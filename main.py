accounts = {}
print("Testing Git")
while True:

    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Create Account Selected")

    elif choice == "2":
        print("Login Selected")

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")