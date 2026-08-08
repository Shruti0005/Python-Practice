#Print all prime numbers from 1 to 100.

for number in range(1, 101):
    fact_check = False
    
    if number == 1:
        fact_check = True
    
    for i in range(2, number):
        if number % i == 0:
            fact_check = True
            break
    
    if not fact_check:
        print(number)

    
    