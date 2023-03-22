def f(number,even):
    num = str(number)
    sum = 0
    if even == True:
        for i in range(len(num)):
            if int(num[i]) % 2 == 0:
                sum += int(num[i])

    elif even == False:
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                sum += int(num[i])

    return(sum)
    