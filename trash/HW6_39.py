array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
x = 0
y = 0
array[0] = [1,2,3,4,5]
for array_mini in array:
    for number in array_mini:
        array_mini[x] = array[0][y] * x
        x += 1
        y += 1
    print(array_mini)
