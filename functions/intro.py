def calculate_credit_score(income, expenses, debt):
    # Calculates a credit score based on income, expenses, and debt
    score = (income - expenses) / debt
    return score

def approve_credit(credit_score, required_score):
    # Approves or denies a credit application based on the credit score
    if credit_score >= required_score:
        return "Credit approved!"
    else:
        return "Credit denied."

# Example usage:
income = 5000
expenses = 2000
debt = 1000
required_score = 2

credit_score = calculate_credit_score(income, expenses, debt)
approval_status = approve_credit(credit_score, required_score)
print(approval_status)