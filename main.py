accounts = {}

def create_account():

    acc_no = input("Enter Account Number: ")
    name = input("Enter Name: ")
    password = input("Enter Password: ")
    balance = float(input("Enter Initial Balance: "))

    accounts[acc_no] = {
        "name": name,
        "password": password,
        "balance": balance
    }

    print("Account Created Successfully")
    print(accounts)


while True:

    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        print("Login Selected")

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")