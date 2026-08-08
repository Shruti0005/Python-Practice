#Check whether a number is a palindrome.
given_number = int(input("Enter number: "))
n = given_number

reverse_digit = 0
while(n > 0):
    digit = n % 10
    reverse_digit = (reverse_digit * 10) + digit
    n //= 10

if reverse_digit == given_number:
    print("Palindrome number")
else:
    print("Not Palindrome number")
