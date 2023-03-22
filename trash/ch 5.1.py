list = []
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    else:
        try:
            list.append(float(number))
        except:
            print('Invalid input')




print(len(list))
for number in len(list):
    sum = sum + number
print(sum / len(list))