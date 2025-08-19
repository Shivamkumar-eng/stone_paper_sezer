import random  # Importing the random module to let the computer make a random choice

# Dictionary to map game choices to numbers
gameCharacters = {"stone": 1, "paper": 2, "scissors": 3}

# Reverse dictionary to convert number back to choice name
reversedict = {1: "stone", 2: "paper", 3: "scissors"}

# Ask for player's name
name = input("Enter your name: ")

# Start an infinite loop to keep the game running until user exits
while True:
    # Ask user for input
    user = input("Enter your choice: \n 1. stone\n 2. paper\n 3. scissors\n 4. exit\n")

    # Check if user entered a valid choice
    if user == "stone" or user == "paper" or user == "scissors" or user == "exit":
        print(f"Hi {name}")
    else:
        print("You entered an invalid input!")
        continue  # Skip rest of loop and ask again

    # If user wants to exit the game
    if user == "exit":
        print("Thanks for playing!")
        break  # Exit the loop

    # Computer randomly selects a choice (1 for stone, 2 for paper, 3 for scissors)
    computer = random.choice([1, 2, 3])

    # Convert user's choice from string to corresponding number
    user_choose = gameCharacters[user]

    # Get the computer's choice name from its number
    computer_choose = reversedict[computer]

    # Display both user and computer choices
    print(f"You entered: {user}")
    print(f"Computer chose: {computer_choose}")

    # Determine the winner using conditions
    if user_choose == 1 and computer == 3:
        print("You win!")
    elif user_choose == 2 and computer == 2:
        print("It's a draw!")
    elif user_choose == 2 and computer == 3:
        print("You lose bro")
    elif user_choose == 3 and computer == 3:
        print("It's a draw!")
    elif user_choose == 1 and computer == 1:
        print("It's a draw!")
    elif user_choose == 3 and computer == 2:
        print("You win!")
    elif user_choose == 1 and computer == 2:
        print("You lose bro")
    elif user_choose == 2 and computer == 1:
        print("You win!")
    elif user_choose == 3 and computer == 1:
        print("You lose!")
