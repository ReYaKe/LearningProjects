import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class DiceRollerApp(QMainWindow):   
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dice Roller")
        self.setGeometry(100, 100, 300, 200)

        self.roll_button = QPushButton("Roll Dice", self)
        self.roll_button.setGeometry(100, 50, 100, 30)
        self.roll_button.clicked.connect(self.roll_dice)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(100, 100, 200, 30)
        

    def roll_dice(self):
        roll = list(range(0,13)) # Create the empty list
        for i in range(1,13): # and fill with empty sets.
            roll[i] = set()
    
        for i in range (1,7):
            for j in range(1,7):
                k = i+j
                roll[k].add((i,j))
             
        winner = roll[7] | roll[11]
        loser = roll[2] | roll[3] | roll[12]
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        val = (die1, die2)
        sumVal = sum(val)

        if val in winner:
            self.result_label.setText(f"Player wins: {sumVal}, {val}")
        elif val in loser:
            self.result_label.setText(f"Player loses: {sumVal}, {val}")
        else:
            self.result_label.setText(f"Point: {sum(val)}")
            point = roll[die1+die2]
            while True:
                die1 = random.randrange(1,7)
                die2 = random.randrange(1,7)
                val = (die1,die2)
                sumVal = sum(val)
                if val in point:
                    self.result_label.setText(f"Player wins: {sumVal}, {val}")
                    break
                elif val in roll[7]:
                    self.result_label.setText(f"Player loses: {sumVal}, {val}")
                    break
                else:
                    self.result_label.setText(f"Player rolls: {sumVal}, {val}, rolling again.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiceRollerApp()
    window.show()
    sys.exit(app.exec_())
