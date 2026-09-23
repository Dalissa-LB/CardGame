import random
from players import CompBlackjackPlayer, HumBlackjackPlayer
from Deck import Deck

class BlackjackManager:

   COMPNAMES = ["Jacob", "Tiffany", "Zeke", "Bella"]


def _init_(self):
      self.usedNames =[]
      dealerName = random.choice(self.COMPNAMES)
      self.dealer = CompBlackjackPlayer
      


def resetGame(self, playerName):
     self.players = []
     human = HumBlackjackPlayer(playerName)
     self.players.append(human)

     # Prompt the number of computer players
     validNumPlayers = False
     while not validNumPlayers:
          print("")
          print("How many computer players would you like to play against? (1-4)")
          numComps = input("------>")

          try:
               numComps = int(numComps) - 1
               if numComps >= 0 and numComps < 5:
                validNumPlayers = True
               else:
                    print("Invalid number - please try again!")
          except ValueError:
               print("Invalid number - please try again!")

# Create  other computers and add them to players list
     if numComps == 0:
          self.players.append(self.dealer)
     else:
          for _ in range(numComps):
               validName = False
               while not validName:
                    compName = random.choice(self.COMPNAMES)
                    if compName not in self.usedNames:
                         validName = True
               computer = CompBlackjackPlayer(compName)
               self.players.append(computer)
               self.usedNames.append(computer)
               self.players.append
              

def determineWinner(self):
     pass    

def promptNextGame(self):
     pass

def manageTurn(self, player):
     takingTurn = True
     handNum = 1
     while takingTurn:

          player.showHand(handNum)
          choice = player.makeChoice(handNum)
          if choice == "split":
               pass
          elif choice == "hit":
               player.drawCard(self.dec.draw(), handNum)
          else:
               takingTurn = False


def playGame(self):
     # Prompt player name and set up game
     print("")
     print("What is your name?")
     playerName = input("---->")
     self.resetGame(playerName)

     # Play the game
     for _ in range(2):
          for player in self.players:
              player.drawCard(self.deck.draw())

     for player in self.players:
          self.manageTurn(player)