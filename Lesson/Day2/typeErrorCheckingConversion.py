num_char = len(input("What is your name? "))
# print("Your name has " + num_char + "characters.") # --> Error

# the uppon commands would saying error:
# TypeError: can only cancatenate str (not "int") to str (string)

# showing type of var
print(type(num_char)) # output: <class 'int'>

# Type conversion:
new_num_char = str(num_char) # convert int to string
print("Your name has " + new_num_char + " characters.")


# from string to float
print("Result from convert form string to number: ", 70 + float("100"))

print("Result from convert from number to string: ", str(70) + str(100))