def f(human_age):
    if int(human_age) <= 2:
        return(int(human_age)*10)
    else:
        return(2*10 + int((human_age-2)*4))
f(15)