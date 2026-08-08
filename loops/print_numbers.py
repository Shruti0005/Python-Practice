#Print numbers from 1 to 10 using a for loop.
for number in range(1, 11):
    print(number)
print("\n-----------------------------")

#Print numbers from 10 to 1 in reverse order.
print("\nreverse number: ") 
for number in range(10, 0, -1):
    print(number)
print("\n-----------------------------")
    
#Print numbers from 1 to 50, but skip 25 using continue.
print("\nPrint number but skip 25: ")
for number in range(1, 51):
    if number == 25:
        continue
    print(number)
print("\n-----------------------------")
    
#Print numbers from 1 to 10, but stop when the number becomes 6 using break.
print("\nStop print number when number becomes 6: ")
for number in range(1, 11):
    if number == 6:
        break
    print(number)

