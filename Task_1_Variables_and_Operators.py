# Caclulates an area of a rectangle

def square_rectangle(length, width):
    if length > 0 and width > 0:
        area_rectangle = width * length 
        print("The area of the rectangle is:", area_rectangle)
    else: 
        raise Exception("Please enter positive numbers for both length and width.")
    
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))  
square_rectangle(length, width)
