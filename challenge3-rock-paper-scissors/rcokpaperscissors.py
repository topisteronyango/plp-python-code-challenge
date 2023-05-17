# Importing the random module
import random
 # Defining the get_user_choice function
def get_user_choice():
    # while loop to repeatedly prompt the user until they enter a valid choice ('rock', 'paper', or 'scissors'
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ")
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")
# Defining the get_computer_choice function
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Defining the determine_winner function
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Start the game with the welcome message
print("Welcome to Rock, Paper, Scissors Game!")

# Prompting the user to enter their choice
user_choice = get_user_choice()

# Generating the computer's choice and print it
computer_choice = get_computer_choice()
print("Computer chooses:", computer_choice)

# Determiinge the winner and printing the result
result = determine_winner(user_choice, computer_choice)
print(result)
