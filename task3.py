import re

def password_complexity_checker(password):
    """Check the complexity of a given password and provide feedback."""
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    criteria_met = [length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria]
    score = sum(criteria_met)
    
    feedback = "Password Strength: "

    if score == 5:
        feedback += "Very Strong"
    elif score == 4:
        feedback += "Strong"
    elif score == 3:
        feedback += "Moderate"
    elif score == 2:
        feedback += "Weak"
    else:
        feedback += "Very Weak"

    suggestions = []
    if not length_criteria:
        suggestions.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        suggestions.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        suggestions.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        suggestions.append("Password should contain at least one number.")
    if not special_criteria:
        suggestions.append("Password should contain at least one special character.")

    return feedback, suggestions

def main():
    print("Password Complexity Checker")
    while True:
        password = input("Enter a password to check: ")
        feedback, suggestions = password_complexity_checker(password)
        
        print(feedback)
        if suggestions:
            print("Suggestions to improve your password:")
            for suggestion in suggestions:
                print(f"- {suggestion}")

        continue_choice = input("Do you want to check another password? (Y/N): ").upper()
        if continue_choice != 'Y':
            break

if __name__ == "__main__":
    main()
