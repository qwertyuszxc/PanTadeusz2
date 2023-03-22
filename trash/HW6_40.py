array_big = [[-38, -19], [5,40],[-7,11],[-12,-16]]
min = 0
max = 0
column = 0
row = 0
for array in array_big:
    for number in array:
        if number > max:
            max = number
        if number < min:
            min = number
    if min in array:
        row_min = array_big.index(array)+1
    if min in array:
        column_min = array.index(min)+1
    if max in array:
        row_max = array_big.index(array)+1
    if max in array:
        column_max = array.index(max)+1
    print(array)
print('Min','row: ',row_min,'column: ', column_min)
print('Max','row: ',row_max,'column: ', column_max)