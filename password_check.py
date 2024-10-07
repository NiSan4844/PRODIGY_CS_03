import re

def assess_password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_character_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Evaluate the password strength
    criteria_met = [length_criteria, uppercase_criteria, lowercase_criteria,
                    number_criteria, special_character_criteria]
    
    strength_score = sum(criteria_met)
    
    # Provide feedback
    if strength_score == 5:
        feedback = "Your password is very strong!"
    elif strength_score == 4:
        feedback = "Your password is strong, but could be improved."
    elif strength_score == 3:
        feedback = "Your password is moderate; consider making it stronger."
    else:
        feedback = "Your password is weak; please improve it."

    return {
        "is_strong": strength_score == 5,
        "strength_score": strength_score,
        "feedback": feedback
    }

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = assess_password_strength(password)
    print(f"Password Strength Score: {result['strength_score']}/5")
    print(result['feedback'])
