# Caclulates an area of a rectangle

class Rectangle: # class - bluepring/model of the object

    def __init__(self, length, width): #  defining properties - variables but in OOP
        self.length = length
        self.width = width

    def square_rectangle(length, width): # defining method with parameters - functions but in OOP
        if length > 0 and width > 0:
            area_rectangle = width * length 
            print("The area of the rectangle is:", area_rectangle)
        else: 
            raise Exception("Please enter positive numbers for both length and width.")
        
Rectangle.square_rectangle(5,8) # calling methond of the class with arguments / calling method on instance (sample of object)
