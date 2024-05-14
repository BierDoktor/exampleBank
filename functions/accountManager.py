account1 = { 'name': 'John', 'balance': 1000 }
account2 = { 'name': 'Steven', 'balance': 2000 }

def deposit(account, amount):
    account['balance'] += amount

    return account

def withdraw(account, amount):
    if account['balance'] < amount:
        print('Insufficient funds')

        return account
    account['balance'] -= amount

    return account

def transfer(sender, recipient, amount):
    withdraw(sender, amount)
    deposit(recipient, amount)

    return sender, recipient

print(deposit(account1, 500))
print(withdraw(account1, 200))
print(transfer(account1, account2, 300))
