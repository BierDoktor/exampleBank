account1 = {"name": "John", "balance": 1000}
account2 = {"name": "Steven", "balance": 2000}


def deposit(account, amount):
    account["balance"] += amount

    return account


def withdraw(account, amount):
    if account["balance"] < amount:
        print("Insufficient funds")

        return False
    account["balance"] -= amount

    return account


def transfer(sender, recipient, amount):
    withdraw(sender, amount)
    deposit(recipient, amount)

    return sender, recipient


###########################################

active = True

while active:
    print("\nDear customer, welcome to the bank.")

    account = None

    try:
        account_number = int(input("Please enter your account number: "))
        account = account1 if account_number == 1 else account2

        print(f'Welcome {account["name"]}')
        print(f'Your balance is {account["balance"]}')

        try:
            choice = int(
                input(
                    "What would you like to do?\n1. Withdraw\n2. Deposit\n3. Transfer"
                    + "\n4. Exit\nPlease enter your choice:"
                )
            )

            match choice:
                case 1:
                    amount = int(input("Enter the amount you want to withdraw: "))
                    account = withdraw(account, amount)

                    if account:
                        print(f'Your new balance is {account["balance"]}')
                case 2:
                    amount = int(input("Enter the amount you want to deposit: "))
                    account = deposit(account, amount)

                    print(f'Your new balance is {account["balance"]}')
                case 3:
                    recipient = account1 if account_number == 2 else account2
                    amount = int(input("Enter the amount you want to transfer: "))
                    sender, recipient = transfer(account, recipient, amount)

                    print(f'{sender["name"]}, your new balance is {sender["balance"]}')
                    print(f'{recipient["name"]}, has received {amount}.')
                case 4:
                    active = False
                case _:
                    print("Please enter a valid choice")

        except ValueError:
            print("Please enter a valid choice")
            continue
    except ValueError:
        print("Please enter a valid account number")
