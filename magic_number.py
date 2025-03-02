import os, random


# Start Game Loop
while True:
    # Clear terminal
    os.system("cls")

    # Game rules
    min_number = 1
    max_number = 10
    try_count = 3

    # Print game intro
    print("-"*50, "The Magic Number Game", "-"*50)
    print(f"I think of a number between {min_number} and {max_number}. Can you guess it?")
    print(f"You have {try_count} tries.")


    # Get a random number between min_number and max_number
    magic_number = 5

    # Get number from player
    player_number = input("What is your guess?")


    if magic_number == player_number:
        print(f"You win! {magic_number} was my number.")
    else:
        print("You lost this round.")


    response = input("Do you want to play again (y/n)")
    if response == "n":
        print("Game Exited. See you later!")
        break