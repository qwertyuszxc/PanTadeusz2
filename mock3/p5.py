class C:

    def __init__(self,name,surname,age,year):
        self.name = name
        self.surname = surname
        self.age = age
        self.year = year

    def __str__(self):
        self.x = ''
        self.x += self.surname + self.name[0] + str(self.year)
        if self.age >= 18:
            self.x = self.x.upper()
        else:
            self.x = self.x.lower()
        return self.x

        



