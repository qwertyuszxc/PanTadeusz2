person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions",],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999",},
   }
print(person)
print(person['name'])
print(person['hobby'])
person['surname']='Nowak'
person['married'] = False
person['gender'] = "male"
person['hobby'].append('bicycle')
person['height'] = 180
person["phone"]['workphone'] = '3131314444'
print(person)
