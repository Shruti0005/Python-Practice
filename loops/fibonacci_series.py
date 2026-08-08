#Generate the first n terms of the Fibonacci series.
given_number = int(input("Enter number: "))
a = 0
b = 1 
next_number = 0

for number in range(given_number):
    print(a)
    next_number = a + b
    a = b
    b = next_number

