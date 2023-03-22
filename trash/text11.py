film_titles = ['Prisoners ','Guilty ','Fight Club ','Bladerunner 2049 ','Driver ']
file=open('Films.txt','w')
for title in film_titles:
    file.write(title + '\n')
file.close()
file = open('Films.txt','r')
print(file.read())
file.close()
