# Check if a given number is even or odd.

number = float(input("Please enter your number: "))

if number > 0:
    if int(number) % 2 == 0:
        print(number, " is even")
    else:
        print(number, " is odd")
else:
    raise Exception("Please enter positive number")
   