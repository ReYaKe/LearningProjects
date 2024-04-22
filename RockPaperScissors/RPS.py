import random
choices = ["rock", "paper", "scissors"]



pWins = 0
pcWins = 0

while True:
    choice = random.choice(choices)
    print ("Rock-paper-scissors: type in your choice:    ")
    player = input().lower()
    if player == choice:
        print ("Game is a tie. Please try again.")
        print ("Current scores:\n  Player: " + str(pWins) + "\n Computer: " + str(pcWins) )
    elif player == "rock":
        if choice == "scissors":
            print ("Congratulations. Computer chose " + choice + ". You win.")
            pWins += 1
            print ("Current scores:\n  Player: " + str(pWins) + "\n Computer: " + str(pcWins) )
        else:
            print ("Sorry - computer chose " + choice + " and wins.")
            pcWins += 1
            print ("Current scores:\n  Player: " + str(pWins) + "\n Computer: " + str(pcWins) )
    elif player == "paper":
        if choice == "scissors":
            print ("Sorry - computer chose " + choice + " and wins.")
            pcWins += 1
            print ("Current scores:\n  Player: " + str(pWins) + "\n Computer: " + str(pcWins) )
        else:
            print ("Congratulations. Computer chose " + choice + ". You win.")
            pWins += 1
            print ("Current scores:\n  Player: " + str(pWins) + "\n Computer: " + str(pcWins) )
    elif player == "scissors":
        if choice == "rock":
            print ("Sorry - Computer chose " + choice + " and wins.")
            pcWins += 1
            print ("Current scores:\n  Player: " + str(pWins) + "\n Computer: " + str(pcWins) )
        else:
            print ("Congratulations. Computer chose " + choice + ". You win.")
            pWins += 1
            print ("Current scores:\n  Player: " + str(pWins) + "\n Computer: " + str(pcWins) )
    elif player == "exit":
        print("Exiting the game. Thanks for playing!")
        break
    else:
        print ("Error: Select one of: rock, paper, scissors")