import re

def check_password_strength(password):
    """
    Assess password strength based on length, uppercase/lowercase letters,
    numbers, and special characters. Returns a strength rating.
    """
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    is_long = len(password) >= 8

    score = sum([has_upper, has_lower, has_digit, has_symbol, is_long])

    if score == 5:
        return "Very Strong — Meets all security requirements."
    elif score == 4:
        return "Strong — Good, but could be improved."
    elif score == 3:
        return "Moderate — Add more complexity."
    else:
        return "Weak — Needs significant improvement."

def show_tips():
    """Print suggestions for creating a strong password."""
    tips = [
        "Use at least 12 characters.",
        "Include uppercase and lowercase letters.",
        "Add numbers and special symbols.",
        "Avoid dictionary words or common patterns.",
        "Do not reuse passwords across accounts.",
        "Consider using a password manager.",
        "Enable Two-Factor Authentication for important accounts."
    ]
    print("Password Security Tips:")
    for tip in tips:
        print("- " + tip)

def main():
    print("=" * 60)
    print("Password Strength Checker")
    print("=" * 60)

    show_tips()
    password = input("\nEnter a password to check: ")

    # Mask password except first and last characters
    if len(password) > 2:
        masked = password[0] + "*" * (len(password) - 2) + password[-1]
    else:
        masked = password

    print(f"\nPassword Entered: {masked}")
    print(check_password_strength(password))

if __name__ == "__main__":
    main()
