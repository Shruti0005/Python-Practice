#Find the smallest digit in a number.
given_number = int(input("Enter number: "))

n = given_number
smallest = 9
while(n > 0):
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10

print(f"Smallest digit in a number is {smallest}.")