#!/usr/bin/env python3
class Square:
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)
        

        #self.width = width
    
    def area(self):
        return self.length * self.length 

    def who_am_i(self):
        return "Square"
    
    

class Rectangle(Square):
    def __init__(self, length, width, **kwargs ):
        self.width = width 
        super().__init__(**kwargs)
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width
    
    def who_am_i(self):
        return "Rectangle"

class Cube(Square):
    def surface_area(self):
        face_area = self.area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return face_area * self.length

    def who_am_i(self):
        return "Cube"

    def family_tree(self):
        return "{} child of {}".format(self.who_am_i(), super().who_am_i()) # Super a short cut for super(Cube, self)
        #This work inside a class mehod through inheritance




# rectangle = Rectangle(4, 4)
# square = Square(4)
# print(rectangle.who_am_i())
# print(square.who_am_i())

# cube = Cube(4)
# print(super(Cube, cube).who_am_i()) # Accessing Parent mehods
# print(cube.family_tree())

# triangle = Triangle(5, 5)
# print(triangle.area())

# rp = Right_pyramid(3, 5)
# print(rp.area())
