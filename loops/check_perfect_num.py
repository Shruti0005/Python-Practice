# Check whether a number is a perfect number. Example: 28 → True

given_number = int(input("Enter number: "))

total = 0
for number in range(1, given_number//2 + 1):
    if given_number % number == 0:
        total += number
        
if given_number == total:
    print("Perfect number")
else:
    print("Not Perfect number")
