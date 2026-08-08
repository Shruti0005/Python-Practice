#Print the multiplication table of 7.
table_number = int(input("Enter number for table: "))

for number in range(1, 11):
    print(f"{table_number} * {number} = {table_number * number}")

