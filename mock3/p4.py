def f(d,n):
    x = ''
    count = 1
    for i in d.values():  
        if i > n:
            y = i
            for k,v in d.items():
                if y == v:
                    count += 1
                    x += k
                    if count > 1:
                        x+= ','
    x = x[:-1]
    return x
