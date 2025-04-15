class friends:
   def __init__ (self, first, last, age, salary):
        self.first = first
        self.last = last
        self.age = age
        self.salary = salary


   def fullname (self):
        return '{}{}'.format(self.first,self.last)


person1 = friends ("Joshua", "Brazil", 20, 100000)
person2 = friends ("Jade", "Padilla", 20, 5000)


print(person1.fullname())
print(person2.fullname())
