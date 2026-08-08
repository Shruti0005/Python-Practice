given_number = int(input("Enter number: "))

n = given_number
largest = 0
second_largest = 0

while n > 0:
    digit = n % 10
    if digit > largest and digit > second_largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit
    n //= 10

print(f"Second largest Digit: {second_largest}")

