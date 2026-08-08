#Count the number of vowels in a string.
given_string = input("Enter string: ")
number_count = 0

for char in given_string:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        number_count += 1
print(number_count)
