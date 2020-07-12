#!/usr/bin/env python3
class Person:
    def __init__(self, name, age, work = "Software engineer"):
        self.name = name
        self.age = age
        self.work = "Software engineer"
    def __str__(self):
        f"{self.name}, {self.age}, {self.work}"
    def eat(self, food):
        print("{} eat {}".format(self.name,food))
    def action(self):
        print("{} like to walk".format(self.name))


class Baby(Person):
    def nap(self):
        print("{} take a nap".format(self.name))
    def speak(self):
        print("{} says bla! bla! bla!".format(self.name))
    
    

person = Person("Dre", 38,)
baby = Baby("Mhikel", 2, "sleep")
print(person.name)
print(person.eat(" Oatmeal"))
print(person.action())
print()
print(baby.name)
print(baby.nap())
print(baby.speak())
