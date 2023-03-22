def f(player1,player2):
    p1 = 0
    p2 = 0
    for card in player1:
        if card == 'A' or card == 'K' or card == 'Q' or card == 'J' or card == 'T':
            p1 += 10
        else:
            p1 += int(card)
    for card1 in player2:
        if card1 == 'A' or card1 == 'K' or card1 == 'Q' or card1 == 'J' or card1 == 'T':
            p2 += 10
        else:
            p2 += int(card1)
    if p1 > p2:
        return(True)
    else:
        return(False)
