accounts = {}

transactions = []


# LOAD ACCOUNTS FROM FILE
def load_accounts():

    try:

        file = open("accounts.txt", "r")

        for line in file:

            data = line.strip().split(",")

            acc_no = data[0]
            name = data[1]
            password = data[2]
            balance = float(data[3])

            accounts[acc_no] = {
                "name": name,
                "password": password,
                "balance": balance
            }

        file.close()

    except FileNotFoundError:

        pass


# SAVE ACCOUNTS TO FILE
def save_accounts():

    file = open("accounts.txt", "w")

    for acc_no in accounts:

        name = accounts[acc_no]["name"]
        password = accounts[acc_no]["password"]
        balance = accounts[acc_no]["balance"]

        file.write(
            f"{acc_no},{name},{password},{balance}\n"
        )

    file.close()


# LOAD TRANSACTIONS
def load_transactions():

    try:

        file = open("transactions.txt", "r")

        for line in file:

            transactions.append(line.strip())

        file.close()

    except FileNotFoundError:

        pass


# SAVE TRANSACTIONS
def save_transactions():

    file = open("transactions.txt", "w")

    for transaction in transactions:

        file.write(transaction + "\n")

    file.close()


# CREATE ACCOUNT FUNCTION
def create_account():

    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:

        print("Account Already Exists")
        return

    name = input("Enter Name: ")
    password = input("Enter Password: ")
    balance = float(input("Enter Initial Balance: "))

    accounts[acc_no] = {
        "name": name,
        "password": password,
        "balance": balance
    }

    save_accounts()

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
            f"Account {acc_no} Deposited Rs.{amount}"
        )

        save_accounts()
        save_transactions()

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
                f"Account {acc_no} Withdrawn Rs.{amount}"
            )

            save_accounts()
            save_transactions()

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


# LOAD DATA WHEN PROGRAM STARTS
load_accounts()
load_transactions()


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