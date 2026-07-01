import sys
import time

def print_header():
    """Prints a clean visual interface header."""
    print("\n" + "="*45)
    print("      STANDARD ARITHMETIC CALCULATOR      ")
    print("="*45)

def print_menu():
    """Displays the available operations to the user."""
    print("\nAvailable Operations:")
    print("  [1] Addition       (+)")
    print("  [2] Subtraction    (-)")
    print("  [3] Multiplication (*)")
    print("  [4] Division       (/)")
    print("  [5] Exit Program")
    print("-" * 45)

def get_number_input(prompt_text):
    """
    Prompts the user for a number and validates the input.
    Repeats until a valid float is entered.
    """
    while True:
        try:
            user_input = input(prompt_text).strip()
            # Allow the user to abort to the main menu
            if user_input.lower() == 'menu':
                return 'menu'
            return float(user_input)
        except ValueError:
            print("  ❌ Invalid input! Please enter a valid numerical value (or type 'menu').")

def perform_calculation(num1, num2, choice):
    """
    Performs the arithmetic operation based on the choice.
    Returns a tuple: (result_string, success_boolean)
    """
    if choice == '1':
        result = num1 + num2
        return f"{num1} + {num2} = {result}", True
        
    elif choice == '2':
        result = num1 - num2
        return f"{num1} - {num2} = {result}", True
        
    elif choice == '3':
        result = num1 * num2
        return f"{num1} * {num2} = {result}", True
        
    elif choice == '4':
        # Defensive check against ZeroDivisionError
        if num2 == 0:
            return "Runtime Error: Division by zero is mathematically undefined.", False
        result = num1 / num2
        return f"{num1} / {num2} = {result}", True
        
    return "Invalid operation choice.", False

def main():
    """Main application loop control."""
    print_header()
    
    while True:
        print_menu()
        choice = input("Select an option (1-5): ").strip()
        
        # 1. Handle Program Exit
        if choice == '5':
            print("\nShutting down calculator... Goodbye!")
            time.sleep(0.5)
            sys.exit(0)
            
        # 2. Validate Menu Choice
        if choice not in ['1', '2', '3', '4']:
            print("  ❌ [Error] Invalid choice. Please pick a number between 1 and 5.")
            continue
            
        # 3. Collect Numerical Inputs
        print("\n--> (Type 'menu' at any prompt to go back)")
        
        num1 = get_number_input("Enter the first number: ")
        if num1 == 'menu': 
            continue
            
        num2 = get_number_input("Enter the second number: ")
        if num2 == 'menu': 
            continue
            
        # 4. Process and Display Results
        print("\nProcessing calculation...")
        time.sleep(0.3)  # Slight delay for user experience realism
        
        display_text, success = perform_calculation(num1, num2, choice)
        
        if success:
            print("\n✨ Calculation Successful! ✨")
            print(f"👉 Result: {display_text}")
        else:
            print(f"\n❌ {display_text}")
            
        print("\n" + "."*45)
        input("Press Enter to continue to the next calculation...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C interruptions
        print("\n\nProgram interrupted by user. Exiting safely.")
        sys.exit(0)
