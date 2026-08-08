#Check whether a number is an Armstrong number.
given_number = int(input("Enter number: "))

n = given_number
digit_count = 0

while n > 0:
    digit_count += 1
    n //= 10

n = given_number
total = 0

while n > 0:
    digit = n % 10
    total += digit ** digit_count
    n //= 10 
print(total)
if given_number == total:
    print("Armstrong Number.")
else:
    print("Not Armstrong Number.")
