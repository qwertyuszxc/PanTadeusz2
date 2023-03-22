def f5(c):
    count = 0
    with open('poem.txt','r') as file:
        f_line = file.readlines()
        for stroka in f_line:
            print(stroka)
            if stroka.find(c) >= 0:
                count+=1
    print(count)
f5('c')