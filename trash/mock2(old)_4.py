def f4(d):
    number = 0
    sum = 0
    for array in d.values():
        for number in array:
            if int(number) >= 5 and int(number) <= 10:
                sum+=int(number)
    print(sum)

f4({'arr1':[2,6,5],'arr2':[7,1],'arr3':[2,9,8,1]})