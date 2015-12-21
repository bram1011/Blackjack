import random
from hand import h
from bot import dealer
from player import p

betAmount = 0
     

def back():
    from main import playgame
    playgame()

def take_bet():
    global p
    global betAmount
    betAmount = raw_input("How much would you like to bet? ")
    try:
        betAmount = int(betAmount)
    except:
        print "Error: Invalid input"
        take_bet()
    else:
        p.set_bet(betAmount)

def deal(isfirst):
    d = dealer()
    if isfirst:
        h.reset_hand()
        d.reset_hand()
    elif isfirst == False:
        pass
    print "Your current total is ",h.get_hand()
    if h.get_hand() == 21:
        print "Wow you got exactly 21!"
        p.add_money(p.get_bet())
        back()
    elif h.get_hand() > 21:
        print "You've busted!"
        p.lose_money(p.get_bet())
        back()
    elif d.sum_of_hand() == 21:
        print "The dealer got 21!"
        p.lose_money(p.get_bet())
        back()
    elif d.sum_of_hand() > 21:
        print "The dealer busted!"
        p.add_money(p.get_bet())
        back()
    draw = raw_input("Would you like to draw a card? ")
    if draw == 'y':
        chance = random.randint(2,14)
        if chance == 11 or chance == 12 or chance == 13:
            print "You got a face card (Worth 10)"
            h.add_card(10)
            d.add_card()
            deal(False)
        elif chance == 14:
            ace_choice = raw_input("You got an ace. Would you like it to be worth 11 or 1? ")
            ace_choice = int(ace_choice)
            h.add_card(ace_choice)
            d.add_card()
            deal(False)
        else:
            print "You got a ",chance
            h.add_card(chance)
            d.add_card()
            deal(False)
            
            
    elif draw == 'n':
        global betAmount
        print "Your total was %s" %(h.get_hand())
        print "The dealer's total was %s" %(d.sum_of_hand())
        if h.get_hand() > d.sum_of_hand():
            print "Congratulations, you won the hand!"
            p.add_money(p.get_bet())
            back()
        elif h.get_hand() < d.sum_of_hand():
            print "Sorry, the dealer won this time. Try again?"
            p.lose_money(p.get_bet())
            back()
        elif h.get_hand() == d.sum_of_hand():
            print "Looks like you tied"
            back()
    else:
        print "Invalid input"
        deal()  
