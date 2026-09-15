from Cards import Card
from random import shuffle

class Deck:

    RANK = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", 
            "King", "Ace"]
    SUIT = ["Clubs", "Hearts", "Spades", "Diamonds"]

    def _init_(self):
        self.reset()

    def _str_(self):
        return "\n".join(str(card) for card in self.drawPile)

    def reset(self):
        self.drawPile = []
        self.discardPile = []
        self.outPile = []

        for suit in self.SUIT:
            for rank in self.RANK:
                newCard = Card(rank, suit)
                self.drawPile.append(newCard)

    def draw(self):
        toGive = self.drawPile.pop(0)
        self.outPile.append(toGive)
        return toGive
    
    def discard(self, toDiscard):
        if toDiscard in self.outPile:
            self.outPile.remove(toDiscard)
            self.discardPile.append(toDiscard)
        else:
            return self.discardPile

    def shuffle(self):
        shuffle(self.drawPile)