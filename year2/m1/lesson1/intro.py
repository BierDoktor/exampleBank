import random
import time

def get_number(prompt):
    """
    Repeatedly prompt the user until they enter a valid integer.
    Demonstrates I/O design, looping, and exception handling for keyboard input.
    """
    while True:
        user_input = input(prompt)              # I/O function
        try:
            value = int(user_input)             # might raise ValueError
            return value
        except ValueError:
            print(f"❌ '{user_input}' is not a valid integer. Please try again.")

def divide(a, b):
    """
    Attempt to divide a by b, handling division by zero.
    Demonstrates try/except for ZeroDivisionError.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("⚠️  Cannot divide by zero; returning None instead.")
        return None
    else:
        return result

def random_sleep():
    """
    Pause execution for a random short duration.
    Shows use of random and time modules.
    """
    delay = random.uniform(0.5, 2.0)          # random float between 0.5 and 2.0 seconds
    print(f"⏱  Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)                         # pause execution

def main():
    print("🔢 Welcome to the Safe Divider Program!")
    # Sequence: prompt for numerator and denominator
    num = get_number("Enter the numerator: ")
    den = get_number("Enter the denominator: ")

    # Branching: check if user wants randomized delay
    use_delay = input("Would you like a random delay before computing? (y/n): ").strip().lower()
    if use_delay == 'y':
        random_sleep()
    else:
        print("➡️  Continuing without delay.")

    # Perform safe division
    result = divide(num, den)

    # Branching: report outcome
    if result is None:
        print("❌ Division was not performed due to an error.")
    else:
        print(f"✅ Result: {num} ÷ {den} = {result}")

    print("👋 Program finished. Goodbye!")

main()