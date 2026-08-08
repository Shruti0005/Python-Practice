#Count how many even and odd digits are present in a number.

given_num = int(input("Enter number: "))
n = given_num

count_even_digit = 0
count_odd_digit = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        count_even_digit += 1
    else:
        count_odd_digit += 1
    n //= 10

print(f"Even digit count is {count_even_digit}.\nOdd digit count is {count_odd_digit}")