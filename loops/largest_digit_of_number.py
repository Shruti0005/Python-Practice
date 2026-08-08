#Find the largest digit in a number.
given_number = int(input("Enter number: "))

n = given_number
largest = 0
while(n > 0):
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10

print(f"Largest digit in a number is {largest}.")