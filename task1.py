import secrets
import string
import sys

def print_header():
    """Displays a clean UI header."""
    print("=" * 45)
    print("       SECURE PASSWORD GENERATOR v2.0       ")
    print("=" * 45)

def get_integer_input(prompt):
    """Ensures the user provides a valid number for length."""
    while True:
        try:
            val = int(input(prompt))
            if val < 4:
                print("[!] Security Tip: Length should be at least 4.")
                continue
            return val
        except ValueError:
            print("[!] Invalid input. Please enter a number.")

def generate_password():
    """Core logic for building the password based on user criteria."""
    print_header()

    # 1. User Input: Length
    length = get_integer_input("Enter desired password length: ")

    # 2. User Input: Complexity
    print("\nSelect Complexity (y/n):")
    use_upper   = input("Include Uppercase? (ABC): ").lower() == 'y'
    use_numbers = input("Include Numbers? (123):   ").lower() == 'y'
    use_symbols = input("Include Symbols? (!@#):   ").lower() == 'y'

    # Build character pool (Always include lowercase by default)
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    # 3. Generate Password
    # We use a loop to ensure at least one character from each selected category is included
    while True:
        password = ''.join(secrets.choice(chars) for _ in range(length))
        
        # Validation: Check if password meets all selected criteria
        if (any(c.islower() for c in password)
            and (not use_upper or any(c.isupper() for c in password))
            and (not use_numbers or any(c.isdigit() for c in password))
            and (not use_symbols or any(c in string.punctuation for c in password))):
            break
            
    return password

def rate_strength(pwd):
    """Provides a basic visual feedback on password strength."""
    length = len(pwd)
    unique_types = 0
    if any(c.islower() for c in pwd): unique_types += 1
    if any(c.isupper() for c in pwd): unique_types += 1
    if any(c.isdigit() for c in pwd): unique_types += 1
    if any(c in string.punctuation for c in pwd): unique_types += 1

    if length >= 12 and unique_types == 4:
        return "⭐⭐⭐⭐⭐ (Excellent)"
    elif length >= 8 and unique_types >= 3:
        return "⭐⭐⭐ (Good)"
    else:
        return "⭐ (Weak - Consider more characters/types)"

def main():
    """Main application loop."""
    try:
        while True:
            generated_pwd = generate_password()
            
            # 4. Display Result
            print("\n" + "-" * 45)
            print(f" GENERATED PASSWORD: {generated_pwd}")
            print(f" STRENGTH ESTIMATE:  {rate_strength(generated_pwd)}")
            print("-" * 45)

            # Play Again / Exit
            choice = input("\nGenerate another? (y/n): ").lower()
            if choice != 'y':
                print("\nStay secure! Goodbye.")
                break
            print("\n" * 2)
            
    except KeyboardInterrupt:
        print("\n\nProgram closed. Stay safe!")
        sys.exit()

if __name__ == "__main__":
    main()
