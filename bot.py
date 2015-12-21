import random

class dealer(object):
    def __init__(self, hand = []):
        self.hand = hand
        
    def add_card(self):        
        chance = random.randint(2, 14)
        if chance == 11 or chance == 12 or chance == 13:
            (self.hand).append(10)
        elif chance == 14:
            if 11 <= sum(self.hand):
                (self.hand).append(11)
            else:
                (self.hand).append(1)
        else:
            (self.hand).append(chance)
            
    def sum_of_hand(self):
        return sum(self.hand)
    
    def reset_hand(self):
        self.hand = []
        
d = dealer()
