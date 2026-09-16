class CompBlackjackPlayer:

    def _init_(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def _repr_(self):
        return self.name    

    def _eq_(self, other):
       if not isinstance(other, type(self)):
           return False
       if self.name != other.name:
           return False
       if len(self.hand) != len(other.hand):
           return False
       else:
           for idx in range(len(self.hand)):
               if self.hand[idx] != other.hand[idx]:
                   return False


           return True

    
               