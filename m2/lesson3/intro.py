# 1. Purpose of the loop construct:
# The loop will allow repeated transactions (withdrawals) until the user exits or the account balance is zero.

print("Welcome to the bank!")

# Initial account balance
balance = int(input("Enter your initial account balance: $"))

# 2. Using the while operator and designing the loop:
# A while loop will run as long as there is money in the account.

# 3. Set the loop condition using logical expressions:
while balance > 0:  # The loop continues while the balance is greater than zero
    print(f"\nYour current balance is: {balance} $")

    # Get withdrawal amount from the user
    withdrawal = int(input("Enter the amount to withdraw (or 0 to exit): $"))

    # 4. Choose appropriate algorithmic structures:
    # If the user chooses to exit by entering 0, break the loop.
    if withdrawal == 0:
        print("Thank you for banking with us!")
        break

    # Check if the withdrawal amount is valid
    if withdrawal > balance:
        print("Insufficient funds! Please enter a smaller amount.")
    else:
        # 5. Necessity of counters:
        # Here, we use the balance itself as a counter, decrementing it with each withdrawal.
        balance -= withdrawal  # Decrease balance by withdrawal amount
        print(f"{withdrawal} $ withdrawn successfully!")

# 6. Confidently program the while loop with counters:
# The loop ends when the balance reaches zero, and a message is displayed.
if balance == 0:
    print("\nYour account balance is now $0. No more transactions can be made.")
print("Goodbye!")
