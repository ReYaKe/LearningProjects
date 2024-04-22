# This program selects a number between 1 and
# 10 and allows a user (player) to guess what
# it is.5
import random
choice = random.randint(1,10) # The number selected by the computer

# Function to get a valid choice from the player
def get_valid_choice():
    while True:
        playerchoice = input("Please guess a number between 1 and 10.\n")
        if playerchoice.isdigit():
            playerchoice = int(playerchoice)
            if 1 <= playerchoice <= 10:
                return playerchoice
            else:
                print("Number must be between 1 and 10. Please re-enter.\n")
        else:
            print("Invalid input. Please enter a Number between 1 and 10.\n")
            
playerchoice = get_valid_choice()

# Check if the player's guess is correct
if choice == playerchoice:
    print("You win!")
else:
    print("Sorry, you lose. The number was: " + str(choice))



# Close the window
input("Press Enter to exit...\n")
