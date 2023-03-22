def f(card_number):
    card_number_str = str(card_number)
    result = ""
    for i in range(len(card_number_str)):
        if i >= 2 and i < 12:
            result += '*'
        else:
            result += card_number_str[i]
    return(result)
            