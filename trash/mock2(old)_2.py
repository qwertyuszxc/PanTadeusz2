def f2(a1,a2):
    counta1=0
    counta2=0
    for number in a1:
        if number / 10 > 1 and number / 10 < 10:
            counta1+=1
    for number in a2:
        if number / 10 > 1 and number / 10 < 10:
            counta2+=1
    if counta1 == counta2:
        print(True)
    else:
        print(False)

f2([23,7,16,34],[1,18,79,20,6,111])