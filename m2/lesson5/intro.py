class BankAccount:
    # A simple BankAccount class to manage deposits, withdrawals, and balance checks.
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        #Deposit money into the account.
        self.balance += amount
        print(f"${amount} deposited successfully. New balance: ${self.balance}")

    def withdraw(self, amount):
        # Withdraw money from the account.
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"${amount} withdrawn successfully. Remaining balance: ${self.balance}")

    def check_balance(self):
        # Display the account balance.
        print(f"Account balance: ${self.balance}")


def main():
    # Main function to manage user interaction with the banking system.
    print("Welcome to Simple Bank!")
    name = input("Enter your name: ")
    account = BankAccount(account_holder=name)

    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Handle user choices
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for using the Bank. Goodbye.")
            break  # Use of the `break` operator to exit the loop
        else:
            print("Invalid choice. Please select a valid option.")



main()