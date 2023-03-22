def f1(a):
    count = 0
    for number in a:
        if number % 2 == 0 and number > 8:
            count+=1
    print(count)

f1([13,7,4,16,3,12,8])