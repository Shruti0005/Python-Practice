#Calculate base^exponent without using ** or pow().

base_num = int(input("Enter base number: "))
exponent_num = int(input("Enter exponent number: "))

power_num = 1

for number in range(1, exponent_num + 1):
    power_num *= base_num
print(power_num)