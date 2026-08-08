#Calculate the sum of digits of a number.
given_number = int(input("Enter number: "))
n = given_number

total = 0
while(n > 0):
    digit = n % 10
    total += digit
    n //= 10
print(f"Summation of digit: {total}")
