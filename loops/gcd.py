#Find the Greatest Common Divisor (GCD) of two numbers using a loop.
#The brute-force for loop solution:

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

gcd = 1

for number in range(1, min(first_number, second_number)+1):
    if first_number % number == 0 and second_number % number == 0:
        gcd = number
print(gcd) 