import random

roll = list(range(0,13)) # Create the empty list
for i in range(1,13): # and fill with empty sets.
    roll[i] = set()
    
for i in range (1,7):
    for j in range(1,7):
        k = i+j
        roll[k].add((i,j))
             
winner = roll[7] | roll[11]
loser = roll[2] | roll[3] | roll[12]

die1 = random.randrange(1,7)
die2 = random.randrange(1,7)

val = (die1,die2)
print("Player rolls:", val)

if val in winner:
    print("Player wins.")
elif val in loser:
    print("Player loses.")
else:
    point = roll[die1+die2]
    print (die1+die2, " is your point.")
    while True:
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        val = (die1,die2)
        sumVal = sum(val)
        if val in point:
            print("Player rolls:", sumVal, val, "Player wins.")
            break
        elif val in roll[7]:
            print("Player rolls:", sumVal, val, "Player loses.")
            break
        else:
            print("Player rolls:", sumVal, val, "Rolling again.")
        
