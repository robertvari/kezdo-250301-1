import os

# Start Game Loop
while True:
    # Clear terminal
    os.system("cls")

    # Print game intro
    print("-"*50, "The Magic Number Game", "-"*50)

    # Game rules
    min_number = 1
    max_number = 10
    try_count = 3




    response = input("Do you want to play again (y/n)")
    if response == "n":
        print("Game Exited. See you later!")
        break