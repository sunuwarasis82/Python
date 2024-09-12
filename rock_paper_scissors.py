import random

# List of possible moves
moves = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(moves)

def get_user_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in moves:
            return choice
        print("Invalid choice, please try again.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
