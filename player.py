class hand(object):
    
    def __init__(self, cards = []):
        self.cards = cards
    
    def add_card(self, card):
        (self.cards).append(card)
        
    def reset_hand(self):
        self.cards = []
        
    def get_hand(self):
        return sum(self.cards)
h = hand()
