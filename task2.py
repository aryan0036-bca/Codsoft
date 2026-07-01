import random
import sys
import time

# Constants for the game choices
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
CHOICES = [ROCK, PAPER, SCISSORS]

# ASCII Art for a nice visual touch
ASCII_ART = {
    ROCK: """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    PAPER: """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    SCISSORS: """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

def clear_screen():
    """Prints newline characters to keep the terminal clean."""
    print("\n" * 3)

def print_banner():
    """Displays the game introduction banner."""
    print("=" * 50)
    print("      WELCOME TO ROCK, PAPER, SCISSORS!      ")
    print("=" * 50)
    print("Rules: Rock crushes Scissors | Scissors cut Paper | Paper covers Rock\n")

def get_user_choice():
    """Prompts the user for their choice and validates the input."""
    while True:
        print("Available choices:")
        print(" -> [R]ock")
        print(" -> [P]aper")
        print(" -> [S]cissors")
        print(" -> [Q]uit game")
        
        user_input = input("Enter your choice: ").strip().lower()
        
        if user_input in ['r', 'rock']:
            return ROCK
        elif user_input in ['p', 'paper']:
            return PAPER
        elif user_input in ['s', 'scissors']:
            return SCISSORS
        elif user_input in ['q', 'quit', 'exit']:
            return "quit"
        else:
            print("\n[!] Invalid input. Please type R, P, S, or Q.\n")

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(CHOICES)

def determine_winner(user, computer):
    """
    Determines the winner of the round.
    Returns: 'tie', 'user', or 'computer' along with a descriptive reason.
    """
    if user == computer:
        return "tie", "Both picked the same!"
    
    # Win conditions for the user
    if (user == ROCK and computer == SCISSORS):
        return "user", "Rock smashes Scissors!"
    elif (user == SCISSORS and computer == PAPER):
        return "user", "Scissors cut Paper!"
    elif (user == PAPER and computer == ROCK):
        return "user", "Paper covers Rock!"
    
    # If it's not a tie and user didn't win, computer wins
    if (computer == ROCK and user == SCISSORS):
        return "computer", "Rock smashes Scissors!"
    elif (computer == SCISSORS and user == PAPER):
        return "computer", "Scissors cut Paper!"
    elif (computer == PAPER and user == ROCK):
        return "computer", "Paper covers Rock!"

def display_round_results(user_choice, computer_choice, winner, reason):
    """Displays the choices made and the outcome of the round with ASCII art."""
    clear_screen()
    print("=" * 50)
    print(f" YOUR CHOICE:\n{ASCII_ART[user_choice]}")
    print(f" COMPUTER'S CHOICE:\n{ASCII_ART[computer_choice]}")
    print("=" * 50)
    
    print(f"Reason: {reason}\n")
    if winner == "user":
        print("🎉 SUCCESS! You win this round! 🎉")
    elif winner == "computer":
        print("❌ DEFEAT! The computer wins this round! ❌")
    else:
        print("🤝 TIE! It's a draw! 🤝")
    print("=" * 50)

def display_scoreboard(scores, rounds):
    """Displays the current status of the series match."""
    print(f"\n--- SCOREBOARD (Round {rounds}) ---")
    print(f" Player Score   : {scores['user']}")
    print(f" Computer Score : {scores['computer']}")
    print(f" Ties            : {scores['ties']}")
    print("-" * 34)

def ask_to_play_again():
    """Asks the user if they want to continue playing."""
    while True:
        choice = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("[!] Please enter 'y' for Yes or 'n' for No.")

def main():
    """Main game loop managing state and flow."""
    # Score tracking dictionary
    scores = {"user": 0, "computer": 0, "ties": 0}
    round_count = 1
    
    clear_screen()
    print_banner()
    
    while True:
        print(f"\n--- ROUND {round_count} ---")
        
        # 1. Get User Input
        user_choice = get_user_choice()
        if user_choice == "quit":
            print("\nExiting game...")
            break
            
        # 2. Get Computer Selection
        print("\nComputer is choosing...")
        time.sleep(0.8) # Dramatic pause
        computer_choice = get_computer_choice()
        
        # 3. Game Logic
        winner, reason = determine_winner(user_choice, computer_choice)
        
        # Update Scores
        if winner == "user":
            scores["user"] += 1
        elif winner == "computer":
            scores["computer"] += 1
        else:
            scores["ties"] += 1
            
        # 4. Display Results
        display_round_results(user_choice, computer_choice, winner, reason)
        display_scoreboard(scores, round_count)
        
        # 5. Play Again Check
        if not ask_to_play_again():
            break
            
        round_count += 1
        clear_screen()

    # Final wrap up sequence
    clear_screen()
    print("=" * 50)
    print("                FINAL GAME OVER                 ")
    print("=" * 50)
    print(f"Total Rounds Played: {round_count}")
    print(f"Final Score -> You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['ties']}")
    print("\nThank you for playing! Have a great day!")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Graceful exit if Ctrl+C is pressed
        print("\n\nGame closed unexpectedly. Goodbye!")
        sys.exit(0)
