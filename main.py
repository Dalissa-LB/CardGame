# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Helper Functions and Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
from Deck import Deck
from players import CompBlackjackPlayer
from Cards import Card
from manager import BlackjackManager




# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Funtion Definition
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    appOn = True
    blackjack = BlackjackManager()

    while appOn:
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("           Game Menu")
        print("")
        print("           1. Blackjack")
        print("")
        print("           Q --> Quit")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        playerChoice = input("---->")

        if playerChoice == "1":
            playingBlackjack = True
            while playingBlackjack:
                playingBlackjack = blackjack.playGame()
        elif playerChoice == "Q":
            appOn = False
        else:
            print("Invalid option!")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Call Function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
