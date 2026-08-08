#Count the number of digits in an integer entered by the user.
give_number = input("Enter numbers: ")
number_count = 0

for number in give_number:
    number_count += 1
print(number_count)