#Reverse an integer (e.g., 12345 → 54321).
given_number = int(input("Enter number: "))
n = given_number

reverse_digit = 0
while(n > 0):
    digit = n % 10
    reverse_digit = (reverse_digit * 10) + digit
    n //= 10
print(reverse_digit)