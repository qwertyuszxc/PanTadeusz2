import re   
def f3(t):
    sum=0
    x=re.findall(r'\b\d{2,3}\b',t)
    for number in x:
        sum+=int(number)
    print(sum)
f3('penis 16, 2, 114 oraz 1014 także 8')