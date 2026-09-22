# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Helper Functions and Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
from Deck import Deck
from players import CompBlackjackPlayer
from Cards import Card



# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Funtion Definition
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    testDeck = Deck()
    player = CompBlackjackPlayer("Andy")

    player.drawCard(testDeck.draw())
    player.drawCard(testDeck.draw())

    print("")
    print("")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Call Function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
