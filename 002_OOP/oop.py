import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-----------------------------------")
# def print_types(data):
#     for i in data:
#         print(i, type(i))
        

# test = [122, 'victor', [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]

# print_types(test)

# class Person:
#     name = "victor"
#     age = 32
    

# person1 = Person()
# person2 = Person()

# print(person1.name)
# Person.job = "developer"
# print(person2.job)

#! class attributes vs instance attributes 

# class Person:
#     company = "clarusway"
    
#     def test(self):
#         print("test")
        
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
        
#     def get_details(self):
#         print(self.name, self.age)
    
#     @staticmethod
#     def salute():
#         print("Hi there!")

# person1 = Person()
# person2 = Person()


# person1.location = "Turkey"
# # print(person2.location)
# person2.age = 25
# print(person1.age)
# print(person2.age)

# person1.test()
# Person.test(person1)
# person1.set_details("barry", 20)
# person1.get_details()
# print(person1.name)

# person1.salute()
# person2.salute()



#! special methods ( init, str)

# class Person:
#     company = "clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
        
#     def get_details(self):
#         print(self.name, self.age)
    
#     def __str__(self):
#         return f"{self.name} - {self.age}"


# person1 = Person("henry", 18)
# # person1.get_details()

# person2 = Person("selçuk", 22)
# # person2.get_details()

# print(person1)
# print(person2)


#! OOP Principles (4 pillars)

#* encapsulation
#* abstraction
#* polymorhism
#* inheritance


#? encapsulation and abstraction
# class Person:
#     company = "clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000
#         self.__id = 3000
        

#     def __str__(self):
#         return f"{self.name} - {self.age}"

#     def get_details(self):
#         print(self.name, self.age)
        

# person1 = Person("henry", 18)
# person1._id = 4000
# print(person1._id)
# print(person1.__id)
# print(person1._Person__id)

# liste = [2,5,3,4,4]
# liste.sort()
# print(liste)

#? inheritance and polymorphism (and multiple inheritance)
class Person:
    company = "clarusway"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def get_details(self):
        print(self.name, self.age)

class Lang:
    def __init__(self, langs):
        self.langs = langs
    
    def display_langs(self):
        print(self.langs)


class Employee(Person, Lang):
    def __init__(self, name, age, path, langs):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        # self.langs = langs
        self.path = path
        Lang.__init__(self, langs)

    def get_details(self):
        # print(self.name, self.age, self.path)
        super().get_details()
        print(self.path)

emp1 = Employee("vic", 32, "FS", ["pyhton", "JS"])
# emp1.get_details()
# emp1.display_langs()


#! inner class

# from django.db import models

# class Article(models.Model):
#     name = models.CharField(max_length=50)
#     author = models.CharField(max_length=50)

#     class Meta:    # standart isim değişmez class Meta:
#         ordering = ["name"]

# print(Employee.mro())
# print(help(Employee))

#!Topics to be Covered:

#* Everything in Python is class
#? Defining class
#* Defining class attributes
#? Difference between class attributes and instance attributes
#* SELF keyword
#? Static methods
#* Special methods (init, str)
#? 4 pillars of OOP:
#     Encapsulation
#     Abstraction
#     Inheritance
#        Multiple inheritance
#     Polymorphism
#        Overriding methods
#* Inner class








print("-----------------------------------")





