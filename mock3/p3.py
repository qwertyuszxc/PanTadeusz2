def f(n):
    x=''
    y=0
    flag = True
    flag2 = True
    dig = 0
    lit = 0
    for i in range(len(n)):
        x = n[i]
        y = n[i-1]
        if x.isdigit():
            dig += 1
        elif x.isupper():
            lit += 1
        else:
            flag = False
    slic = n[int(y):]
    for i in range(len(slic)):
        if not slic[i].isdigit():
            flag2 = False
    if lit < 1 or lit > 3 or dig < 3 or dig > 5 or n[0] != 'K' or flag != True or flag2 != True:
        return False
    else:
        return True
    
            


    
