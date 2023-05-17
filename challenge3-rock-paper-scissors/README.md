# SOLUTION STEPS
    STEP1: Importing the random module to generate the computer's choice.

    STEP2: Define the get_user_choice function:

        Prompt the user to enter their choice (rock, paper, or scissors).
        Use a while loop to repeatedly prompt the user until a valid choice is entered.
        Return the user's choice.
    
    STEP3: Define the get_computer_choice function:

        Create a list of choices: rock, paper, scissors.
        Use the random.choice function to select a random choice from the list.
        Return the computer's choice.
    STEP4: Define the determine_winner function:

        Take the user's choice and the computer's choice as input parameters.
        If the user's choice is the same as the computer's choice, return "It's a tie!".
        Otherwise, check the following conditions to determine the winner:
            If the user chooses rock and the computer chooses scissors, or
            If the user chooses paper and the computer chooses rock, or
            If the user chooses scissors and the computer chooses paper,
                Return "You win!".
            If none of the above conditions are met, return "Computer wins!".
    STEP5: Start the game with a welcome message.

    STEP6: Call the get_user_choice function to prompt the user to enter their choice. Store the user's choice in a variable.

    STEP7: Call the get_computer_choice function to generate the computer's choice. Print the computer's choice.

    STEP8: Call the determine_winner function with the user's choice and the computer's choice to determine the winner. Store the result in a variable.

    STEP9: Print the result to display the winner of the game.

 # Assumptions:
    The user's input is case-sensitive. The code expects the user to enter their choice as "rock", "paper", or "scissors" exactly as specified, with the correct casing. For example, "Rock" or "ROCK" may not be considered valid choices.








