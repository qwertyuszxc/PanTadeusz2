array = [5, 30, 40, 6, 1]
max = 0
new_max = 0
for number in array:
    if number > max:
        max = number
array.remove(max)
for number in array:
    if number > new_max:
        new_max = number
print(new_max)