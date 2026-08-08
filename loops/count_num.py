#Count how many numbers are divisible by 3 between 1 and 100.
number_count = 0
for number in range (1, 101):
    if number % 3 == 0:
        number_count += 1

print(number_count)
