accounts = {}

# CREATE ACCOUNT FUNCTION
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


# LOGIN FUNCTION
def login():

    acc_no = input("Enter Account Number: ")
    password = input("Enter Password: ")

    if acc_no in accounts:

        if accounts[acc_no]["password"] == password:
            print("Login Successful")

        else:
            print("Incorrect Password")

    else:
        print("Account Does Not Exist")


# DEPOSIT FUNCTION
def deposit():

    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Deposit: "))

    if acc_no in accounts:

        accounts[acc_no]["balance"] += amount

        print("Amount Deposited Successfully")
        print("Updated Balance:", accounts[acc_no]["balance"])

    else:
        print("Account Does Not Exist")


# WITHDRAW FUNCTION
def withdraw():

    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Withdraw: "))

    if acc_no in accounts:

        if accounts[acc_no]["balance"] >= amount:

            accounts[acc_no]["balance"] -= amount

            print("Withdrawal Successful")
            print("Remaining Balance:", accounts[acc_no]["balance"])

        else:
            print("Insufficient Balance")

    else:
        print("Account Does Not Exist")


# MAIN PROGRAM
while True:

    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        login()

    elif choice == "3":
        deposit()

    elif choice == "4":
        withdraw()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")