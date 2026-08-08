#Reverse a string using a loop.
given_string = input("Enter string here: ")
placeHolder = ""
for char in given_string:
    placeHolder = char + placeHolder

print(placeHolder)
