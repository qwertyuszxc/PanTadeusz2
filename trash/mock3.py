def f(array2D):
    numbers = []
    sum = 0
    numbers_sum=[]
    for i in array2D:
        for number in i:
            numbers.append(number)
    for j in range(len(numbers)):
        if j == 0 or j == 4 or j == 8 or j == 12:
            sum += numbers[j]
    numbers_sum.append(sum)
    sum=0
    for j in range(len(numbers)):

        if j == 1 or j == 5 or j == 9 or j == 13:
            sum += numbers[j]
    numbers_sum.append(sum)
    sum=0
    for j in range(len(numbers)):

        if j == 2 or j == 6 or j == 10 or j == 14:
            sum += numbers[j]
    numbers_sum.append(sum)
    sum=0
    for j in range(len(numbers)):
        if j == 3 or j == 7 or j == 11 or j == 15:
            sum += numbers[j]
    numbers_sum.append(sum)

    return(numbers_sum)

f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) 