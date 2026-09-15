class Card:
    def _init_(self, rank="Two", suit="Clubs"):
        self.rank = rank
        self.suit = suit

    def _repr_(self):
        return f"{self.rank} of {self.suit}"
    