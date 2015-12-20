from player import p

def import_deal():
    import dealing
    dealing.take_bet()
    dealing.deal(True)

def endgame():
    print "Hope you had fun! Bye!"

def playgame():
    print "You have $%s" %(p.get_money())
    import_deal()

playgame()
