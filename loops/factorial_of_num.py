#Find the factorial of a given number (e.g., 5! = 120).
given_num = int(input("Enter the number: "))
fact = 1
for number in range(1, given_num + 1):
    fact *= number

print(fact)
