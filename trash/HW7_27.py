import re
with open('grade.txt','r') as file:
    sum = 0
    f = file.read()
    x = re.findall('\d\.\d',f)
    for i in x:
        sum += float(i)
        avg = sum/(len(x)+1)
    print(avg)
file.close()