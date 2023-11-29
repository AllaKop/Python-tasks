# Generates and prints the first 5 multiples of a given number.

user_number = int(input("Please enter your number: "))
amount_of_multiples = int(input("Please enter number of multiples "))

for i in range(amount_of_multiples):
    number = user_number
    number = user_number * (i+1)
    print(number)