f = open('numbers.txt','w')
for i in range(1,51):
    f.write(f'{str(i)}\n')

f.close()