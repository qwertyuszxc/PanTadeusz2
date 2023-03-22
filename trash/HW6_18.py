array = [15, 8, 31, 47, 2, 19]
sum = 0
for number in array:
    sum += number
    print(sum/(array.index(number)+1))