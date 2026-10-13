import random


class CompBlackjackPlayer:

    CARDVALUES ={"Two" :2, "Three" :3, "Four" :4, "Five" :5, "Six" :6, "Seven" :7,
                 "Eight" :8, "Nine" :9, "Ten" :10, "Jack" :10, "Queen" :10, "King" :10,
                 "Ace" :11}

    def _init_(self, name):
        self.name = name
        self.hand = {1: []}
        self.score = {1: 0}

    def _repr_(self):
        return self.name    

    def _eq_(self, other):
       if not isinstance(other, type(self)):
           return False
       if self.name != other.name:
           return False
       if len(self.hand.keys()) != len(other.hand.keys()):
           return False
       else:
           for key in self.hand.keys():
               if len(self.hand[key]) != len(other.hand.key[key]):
                   return False
               else:
                   for idx in range(len(self.hand[key])):
                        if self.hand[key][idx] != self.hand[key][idx]:
                           return False
           return True    

    
def drawCard(self, toGet, handNum=1):
    self.hand[handNum].append(toGet)

def discardCard(self, idx=0, handNum=1):
    return self.hand[handNum].pop(idx)

def showHand(self, handNum=1):
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print(f"             {self.name.upper()}'s Hand")
    print("")
    if len(self.hand[handNum]) ==0:
        print("         No cards in hand!")
    else:
        print("         1. ??? of ???")
        for idx in range(1, len(self.hand[handNum])):
            print(f"            {idx + 1} {str(self.hand[handNum][idx])}")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

    def calcScore(self, handNum=1):
        rawScore = 0
        aces = 0
        for card in self.hand[handNum]:
            rawScore += self.CARDVALUES[card.rank]
            if card.rank == "Ace":
                aces += 1

        while rawScore > 21 and aces > 0:
            rawScore -= 10
            aces -= 1

        self.scores[handNum] = rawScore

    def giveScore(self, handNum=1):
        return self.scores[handNum]

    def makeChoice(self,handNum=1):
        if self.hand[handNum][0] == self.hand[handNum][1]:
            return "split"
        self.calcScore(handNum)
        if self.scores[handNum] >= 17 or len(self.hand[handNum]) == 5:
            return "stay"
        else:
            return "hit"



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HumBlackjackPlayer(CompBlackjackPlayer):

    def showHand(self, handNum=1):
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print(f"             {self.name.upper()}'s Hand")
        print("")
        if len(self.hand[handNum]) ==0:
            print("         No cards in hand!")
        else:
            for idx in range(1, len(self.hand[handNum])):
                print(f"            {idx + 1}. {str(self.hand[handNum][idx])}")
            print("")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")

    def makeChoice(self, handNum=1):
        self.calcScore(handNum)
        if self.score[handNum] >= 21 or len(self.hand[handNum]) == 5:
            return "stay"
        else:
            return input("---->").lower()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
#                            Go Fish Players
#
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class CompGoFishPlayer:

    def __init__(self, name):
        self.name = name
        self.hand = {"Two": [],
                     "Three": [],
                     "Four": [],
                     "Five":[],
                     "Six": [],
                     "Seven": [],
                     "Eight": [],
                     "Nine": [],
                     "Ten": [],
                     "Jack": [],
                     "Queen": [],
                     "King":[],
                     "Ace":[]}
        self.sets = {}
    # Keep these dictionaries between turns.
        self.request_history = {}
        self.request_memory = {}

    def __repr__(self):
        return self.name

    def drawCard(self, goCard):
        cardRank = goCard.rank
        self.hand[cardRank].append(goCard)

    def goFish(self, deckSize):
        choice = random.randint(1, 3)
        if choice  == 1:
            return 0
        elif choice == 2:
            return (deckSize // 2) - 1
        else:
            return deckSize - 1

    def giveSet(self, cardRank):
        toGive = self.hand[cardRank]
        self.hand[cardRank] = []
        return toGive

    def makeChoice(self, players):
        # Find the ranks that the computer currently holds.
        available_ranks = [
            rank for rank, cards in self.hand.items()
            if len(cards) > 0
        ]

        if not available_ranks:
            return None, None

        # Remember previous requests and their outcomes.
        # Prefer ranks that have not been asked for recently.
        choice = []

        for rank in available_ranks:
            for player in players:
                if player == self:
                    continue

                # Store history using the player's name and rank.
                previous = self.request_history.get(
                    (player.name, rank)
                )

                # Prefer opponents known to have this rank.
                if previous == "yes":
                    score = 3
                elif previous == "no":
                    score = 0
                else:
                    score = 1

                choice.append((score, player, rank))

            if not choice:
                return None, None

            # Select the highest-scoring available choice.
            best_score = max(choice[0] for choice in choice)

            best_choice = [
                choice for choice in best_choice
                if choice [0] == best_score
            ]

            _, target_player, chosen_rank = random.choice(best_choice)

            return target_player, chosen_rank

    def rememberRequest(self, player, cardRank, hadCards):
        result = "yes" if hadCards else "no"

        self.request_history[(player.name, cardRank)] = result

        # Keep a second record of the last known result.
        self.request_memory.setdefault(player.name, {})
        self.request_memory[player.name][cardRank] = result
    

    def showMatches(self):
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print(f"             {self.name.upper()}'s Matches")
        print("")
        if len(self.sets.keys()) == 0:
            print("        No matching sets!")
        else:
            for rank in self.sets.keys():
                print(f"          {rank}s: {self.sets[rank]}")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")



class HumGoFishPlayer(CompGoFishPlayer):

    def goFish(self, deckSize):
        validChoice = False
        while not validChoice:
            mid = (deckSize // 2)- 1
            last = deckSize - 1

            print("")
            print(f"Would you like to draw from the top, center, or bottom of deck?")
            playerChoice = input("---->").lower()

            if playerChoice in ["top", "1", "beginning","default"]:
                choiceIDX = 0
                validChoice = True
            elif playerChoice in ["center", "mid", "middle"]:
                choiceIDX = mid
                validChoice = True
            elif playerChoice in ["bottom", "last", "deep sea"]:
                choiceIDX = last
                validChoice = True
            else:
                print("You can't fish here! Cast a line somewhere else!")

        return choiceIDX

    def makeChoice(self, otherPlayers):
        validCardChoice = False
        while not validCardChoice:
            self.showHand()
            cardChoice = input("---->").lower().capitalize()
            
            validCards = []
            for rank in self.hand.keys():
                if len(self.hand)[rank] > 0:
                    validCards.append(rank)
            
            if cardChoice in self.hand.keys():
                validCardChoice = True
            else:
                print("You don't have that card! Pick again!")
            


        validplayerChoice = False
        while not validplayerChoice:
            print(otherPlayers)
            print("Choose a player to ask:")
            playerChoice = input("---->").lower().capitalize()

            if playerChoice in otherPlayers:
                validPlayerChoice = True
            else:
                print(f"There's nobody here named {playerChoice}! Pick again!")

        return [cardChoice, playerChoice]

            
        print("")
        print("")

    def showHand(self):
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print(f"                   {self.name.upper()}'s Hand")
        print("")
        for rank in self.hand.keys():
            if len(self.hand[rank]) > 0:
                print(f"               {rank}: {len(self.hand[rank])}")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")

