from tkinter import *
from tkinter import messagebox

accounts = {}
transactions = []


# ---------------- LOAD ACCOUNTS ----------------
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


# ---------------- SAVE ACCOUNTS ----------------
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


# ---------------- LOAD TRANSACTIONS ----------------
def load_transactions():

    try:

        file = open("transactions.txt", "r")

        for line in file:

            transactions.append(line.strip())

        file.close()

    except FileNotFoundError:

        pass


# ---------------- SAVE TRANSACTIONS ----------------
def save_transactions():

    file = open("transactions.txt", "w")

    for transaction in transactions:

        file.write(transaction + "\n")

    file.close()


# ---------------- CREATE ACCOUNT ----------------
def create_account():

    acc_no = entry_acc.get()

    if acc_no in accounts:

        messagebox.showerror(
            "Error",
            "Account Already Exists"
        )

        return

    name = entry_name.get()
    password = entry_password.get()
    balance = float(entry_balance.get())

    accounts[acc_no] = {
        "name": name,
        "password": password,
        "balance": balance
    }

    save_accounts()

    messagebox.showinfo(
        "Success",
        "Account Created Successfully"
    )


# ---------------- LOGIN ----------------
def login():

    acc_no = entry_acc.get()
    password = entry_password.get()

    if acc_no in accounts:

        if accounts[acc_no]["password"] == password:

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

        else:

            messagebox.showerror(
                "Error",
                "Incorrect Password"
            )

    else:

        messagebox.showerror(
            "Error",
            "Account Does Not Exist"
        )


# ---------------- DEPOSIT ----------------
def deposit():

    acc_no = entry_acc.get()

    amount = float(entry_amount.get())

    if acc_no in accounts:

        accounts[acc_no]["balance"] += amount

        transactions.append(
            f"Account {acc_no} Deposited Rs.{amount}"
        )

        save_accounts()
        save_transactions()

        messagebox.showinfo(
            "Success",
            f"Amount Deposited\nBalance = Rs.{accounts[acc_no]['balance']}"
        )

    else:

        messagebox.showerror(
            "Error",
            "Account Does Not Exist"
        )


# ---------------- WITHDRAW ----------------
def withdraw():

    acc_no = entry_acc.get()

    amount = float(entry_amount.get())

    if acc_no in accounts:

        if accounts[acc_no]["balance"] >= amount:

            accounts[acc_no]["balance"] -= amount

            transactions.append(
                f"Account {acc_no} Withdrawn Rs.{amount}"
            )

            save_accounts()
            save_transactions()

            messagebox.showinfo(
                "Success",
                f"Withdrawal Successful\nBalance = Rs.{accounts[acc_no]['balance']}"
            )

        else:

            messagebox.showerror(
                "Error",
                "Insufficient Balance"
            )

    else:

        messagebox.showerror(
            "Error",
            "Account Does Not Exist"
        )


# ---------------- CHECK BALANCE ----------------
def check_balance():

    acc_no = entry_acc.get()

    if acc_no in accounts:

        messagebox.showinfo(
            "Balance",
            f"Current Balance = Rs.{accounts[acc_no]['balance']}"
        )

    else:

        messagebox.showerror(
            "Error",
            "Account Does Not Exist"
        )


# ---------------- TRANSACTION HISTORY ----------------
def show_transactions():

    if len(transactions) == 0:

        messagebox.showinfo(
            "Transactions",
            "No Transactions Available"
        )

    else:

        history = ""

        for transaction in transactions:

            history += transaction + "\n"

        messagebox.showinfo(
            "Transaction History",
            history
        )


# ---------------- LOAD DATA ----------------
load_accounts()
load_transactions()


# ---------------- MAIN WINDOW ----------------
root = Tk()

root.title("Bank Account Simulation")

root.geometry("500x700")

root.configure(bg="lightblue")


# ---------------- HEADING ----------------
heading = Label(
    root,
    text="BANK ACCOUNT SYSTEM",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue"
)

heading.pack(pady=20)


# ---------------- ACCOUNT NUMBER ----------------
Label(
    root,
    text="Account Number",
    font=("Arial", 12),
    bg="lightblue"
).pack()

entry_acc = Entry(root, font=("Arial", 12))

entry_acc.pack(pady=5)


# ---------------- NAME ----------------
Label(
    root,
    text="Name",
    font=("Arial", 12),
    bg="lightblue"
).pack()

entry_name = Entry(root, font=("Arial", 12))

entry_name.pack(pady=5)


# ---------------- PASSWORD ----------------
Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="lightblue"
).pack()

entry_password = Entry(
    root,
    show="*",
    font=("Arial", 12)
)

entry_password.pack(pady=5)


# ---------------- INITIAL BALANCE ----------------
Label(
    root,
    text="Initial Balance",
    font=("Arial", 12),
    bg="lightblue"
).pack()

entry_balance = Entry(root, font=("Arial", 12))

entry_balance.pack(pady=5)


# ---------------- AMOUNT ----------------
Label(
    root,
    text="Amount",
    font=("Arial", 12),
    bg="lightblue"
).pack()

entry_amount = Entry(root, font=("Arial", 12))

entry_amount.pack(pady=5)


# ---------------- BUTTONS ----------------
Button(
    root,
    text="Create Account",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=20,
    command=create_account
).pack(pady=10)


Button(
    root,
    text="Login",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    width=20,
    command=login
).pack(pady=10)


Button(
    root,
    text="Deposit",
    font=("Arial", 12, "bold"),
    bg="orange",
    fg="white",
    width=20,
    command=deposit
).pack(pady=10)


Button(
    root,
    text="Withdraw",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=20,
    command=withdraw
).pack(pady=10)


Button(
    root,
    text="Check Balance",
    font=("Arial", 12, "bold"),
    bg="purple",
    fg="white",
    width=20,
    command=check_balance
).pack(pady=10)


Button(
    root,
    text="Transaction History",
    font=("Arial", 12, "bold"),
    bg="brown",
    fg="white",
    width=20,
    command=show_transactions
).pack(pady=10)


Button(
    root,
    text="Exit",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white",
    width=20,
    command=root.destroy
).pack(pady=20)


# ---------------- RUN WINDOW ----------------
root.mainloop()