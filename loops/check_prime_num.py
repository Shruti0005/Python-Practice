#Check whether a number is prime.
given_num = int(input("Give number to check prime: "))
fact_check = False

if given_num == 1:
    fact_check = True

for number in range(2, given_num):
    if given_num % number == 0:
        fact_check = True
        break
        
if not fact_check:
    print("Prime number")
else:
    print("Not Prime number")
