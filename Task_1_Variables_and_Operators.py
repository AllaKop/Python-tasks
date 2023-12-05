
import numpy as np

class Shape():
    
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Rectangle(Shape): 

    def __init__(self, length, width): 
        self.length = length
        self.width = width

    def calculate_area(self):
        if self.length > 0 and self.width > 0:
            area_rectangle = self.width * self.length 
            print("The area of the rectangle is:", area_rectangle)
        else: 
            raise Exception("Please enter positive numbers for both length and width.")

    def calculate_perimeter(self):
        if self.length > 0 and self.width > 0:
            perimeter_rectangle = 2 * (self.width + self.length)
            print("The perimeter of the rectangle is:", perimeter_rectangle)
        else: 
            raise Exception("Please enter positive numbers for both length and width.") 

class Circle(Shape):

    def __init__(self, radius): 
        self.radius = radius

    def calculate_area(self):
        if self.radius > 0:
            area_circle = np.pi * (self.radius * self.radius)
            print("The area of the circle is:", area_circle)
        else: 
            raise Exception("Please enter positive number for radius")

    def calculate_perimeter(self):
        if self.radius > 0:
            perimeter_circle = 2 * np.pi * self.radius
            print("The perimeter of the circle is:", perimeter_circle)
        else: 
            raise Exception("Please enter positive number for radius") 
        
rectangle = Rectangle(5, 8)
circle = Circle(6)

figures = [rectangle, circle]

for f in figures:
    f.calculate_area()
    f.calculate_perimeter()
