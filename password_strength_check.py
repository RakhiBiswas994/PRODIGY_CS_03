import re

def password_strength_check(password):
    strength = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

     # Uppercase & Lowercase Combined Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    #Strength password
    if strength == 4:
        verdict = "Strong Password"
    elif strength >= 3:
        verdict = "Moderate Password"
    else:
        verdict = "Weak Password"

    return verdict, feedback


# Take input from user
user_password = input("Enter your password: ")
verdict, suggestions = password_strength_check(user_password)
print(f"\nPassword Strength: {verdict}")
if suggestions:
    print("\nSuggestions to Improve:")
    for item in suggestions:
        print(item)



