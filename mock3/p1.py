def f(n):
    x = ''
    sto = n//100
    dzie = (n - sto*100)//10
    jed = n - (dzie*10)-(sto*100)
    for i in range(sto):
        x += '*'
    for j in range(dzie):
        x += '+'
    for k in range(jed):
        x += '/'
    return x
