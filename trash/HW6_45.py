twoD = [[2,1],[3,5],[7,4],[2,6]]
oneD = []
i=0
for array in twoD:
    for i in range(len(array)):
        x = array.pop()
        oneD.append(x)
print(oneD)