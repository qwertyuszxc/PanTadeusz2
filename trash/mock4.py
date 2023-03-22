def f(dictionary,x,y):
    sum = 0
    for i in dictionary.values():
        for j in i:
            if int(j) <= int(y) and int(j) >= int(x):
                sum += j
    print(sum)
f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10) 