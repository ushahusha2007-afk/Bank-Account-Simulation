accounts = {}

transactions = []

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

        transactions.append(
            f"Account {acc_no} Deposited ₹{amount}"
        )

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

            transactions.append(
                f"Account {acc_no} Withdrawn ₹{amount}"
            )

            print("Withdrawal Successful")
            print("Remaining Balance:", accounts[acc_no]["balance"])

        else:
            print("Insufficient Balance")

    else:
        print("Account Does Not Exist")


# CHECK BALANCE FUNCTION
def check_balance():

    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:

        print("Current Balance:", accounts[acc_no]["balance"])

    else:
        print("Account Does Not Exist")


# TRANSACTION HISTORY FUNCTION
def transaction_history():

    if len(transactions) == 0:

        print("No Transactions Available")

    else:

        print("\n===== TRANSACTION HISTORY =====")

        for transaction in transactions:

            print(transaction)


# MAIN PROGRAM
while True:

    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Exit")

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
        check_balance()

    elif choice == "6":
        transaction_history()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")