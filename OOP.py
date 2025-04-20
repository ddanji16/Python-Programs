class Account:
    def __init__(self, account_number, firstname,lastname, contact,balance=0):
        self.account_number = account_number
        self.firstname = firstname
        self.lastname = lastname
        self.contact=contact
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def get_details(self):
        return {
            "Account Number": self.account_number,
            "Firstname": self.firstname,
            "Lastname": self.lastname,
            "Contact": self.contact,
            "Balance": self.balance
        }

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, firstname,lastname,contact, initial_deposit=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, firstname,lastname,contact, initial_deposit)
            return True
        return False

    def deposit_amount(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return account.deposit(amount)
        return False

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_details()
        return None

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        return None


# Function to display account details
def display_account_details(details):
    if details:
        print("\nAccount Details:")
        for key, value in details.items():
            print(f"{key}: {value}")
    else:
        print("Account not found.")

# Create an instance of the Bank class
bank = Bank()

# Main program loop
while True:
    print("\n1. Add Account")
    print("2. Deposit Amount")
    print("3. View Account Details")
    print("4. Exit")
    choice = input("Choose your desired transaction: ")

    if choice == '1':
        account_number = input("Enter account number: ")
        firstname = input("Enter account holder's firstname: ")
        lastname = input("Enter account holder's lastname: ")
        contact = input("Enter account holder's contact number: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        if bank.add_account(account_number, firstname,lastname,contact, initial_deposit):
            print("Account added successfully!")
        else:
            print("Account number already exists.")

    elif choice == '2':
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        if bank.deposit_amount(account_number, amount):
            print("Amount deposited successfully!")
        else:
            print("Account not found or invalid amount.")

    elif choice == '3':
        account_number = input("Enter account number: ")
        details = bank.get_account_details(account_number)
        display_account_details(details)

    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")