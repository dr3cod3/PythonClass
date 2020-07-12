#!/usr/bin/env python3
import sys
sys.path.append('./shapes')
from shapes import Square
class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)
    
    def triangle_area(self):
        return 0.5 * self.base * self.height
    
    def who_am_i(self):
        return "Triangle"


class Right_pyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)
        return "Right_Pyramid"


triangle = Triangle(5, 5)
print(triangle.triangle_area())

rp = Right_pyramid(3, 5)
print(rp.area())
print(super(Right_pyramid, rp).who_am_i())
