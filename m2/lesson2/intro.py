def check_grade(score):
    """Checks a student's score and assigns a grade.

    Args:
        score: The student's score.

    Returns:
        The assigned grade as a string.
    """

    if score >= 90:
        return "Sehr gut"
    elif score >= 80:
        return "Gut"
    elif score >= 70:
        return "Befriedigend"
    elif score >= 60:
        return "Ausreichend"
    else:
        return "Mangelhaft"

# Example usage:
score = 85
grade = check_grade(score)
print(f"Your grade is: {grade}")