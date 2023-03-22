file = open('products.txt','a')
product=input('What do you want to add? ')
file.write(product + '\n')
file.close

file = open('products.txt','r')
print(file.read())
file.close()