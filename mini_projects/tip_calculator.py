print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_pepole = int(input("How many people to split the bill? "))

tip_as_percentage = tip / 100
total_tip = tip_as_percentage * total_bill
total_bill_include_tip = total_tip + total_bill
split_per_person = total_bill_include_tip / number_of_pepole

print(f"Each person should pay: ${split_per_person}")

