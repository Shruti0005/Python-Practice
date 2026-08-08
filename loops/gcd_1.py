#Find the Greatest Common Divisor (GCD) of two numbers using a loop.
#Euclidean Algorithm:

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

while second_number > 0:
    first_number, second_number = second_number, first_number % second_number

print(first_number)
