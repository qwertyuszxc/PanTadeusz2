def f(amount_to_pay):
    coin5 = amount_to_pay // 5 
    coin2 = (amount_to_pay-coin5*5) // 2
    coin1 = (amount_to_pay - coin5*5 -coin2*2) // 1
    return(coin5+coin2+coin1)
