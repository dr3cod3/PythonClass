#!/usr/bin/env python3
class Dog:
    species = "Mammal"
    def __init__(self, name, age, size,  color):
        self.name = name
        self.age = age
        self.size = size
        self.color = color
    def __str__(self):
       return  f"{self.name}, is {self.age}yrs, {self.size}, and {self.color} color"
    def talk(self):
        print(f"{self.name} says graff! graff! graff!")
    
        

dogs = [Dog("Lucie", 9, "Large", "Brown"), Dog("Bingo", 4, "Small", "Black")]


print()
for dog in dogs:
    print(dog)
    if dog.species == "Mammal":
        #print(dog)
        print(dog.name, "is a  {}".format(dog.species ))
        print(dog.talk())
        print()
