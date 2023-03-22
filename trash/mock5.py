import re
def f(first_letter,last_letter):
    with open('test.txt','r',encoding='utf8') as file:
        f = file.read()
        number = 0
        list = re.findall(r'\b{first_letter}\w*{last_letter}\b',f)
        number = len(list) + 1
        print(list)


f('w','d')