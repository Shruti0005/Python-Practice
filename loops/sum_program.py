#Find the sum of numbers from 1 to 100.
total = 0
for number in range(1, 101):
    total += number
    
print(f"Summation of Natural number: {total}")

#Find the sum of all even numbers between 1 and 50.
total_even = 0
for number in range(2, 51, 2):
    total_even += number
print(f"Summation of Even number: {total_even}")

#Find the sum of all odd numbers between 1 and 50.
total_odd = 0
for number in range(1, 51, 2):
    total_odd += number
print(f"Summation of Odd number: {total_odd}")