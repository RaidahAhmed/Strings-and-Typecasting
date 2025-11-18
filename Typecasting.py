# What is the type of the result when you add an integer 7 to a float 2.3?
num_int = 7  # integer
num_float = 2.3  # float
result = num_int + num_float
print(result)
print(type(result))
# The result will be a float.
# Try this code and predict the output:
x = 4  # Integer
y = 5.0  # Float
z = x + y
print(z, type(z))
# The result will be a float
# Convert the string "250" into an integer and subtract 50. What is the result?
num_str = "250"
Num_int = int("250")
# Coverts the string to an integer.
Result = Num_int - 50
print(Result)
# What happens if you try int("hello")? Explain.
Word = "hello"
# print(int(Word))
# invalid literal for int() with base 10: 'hello'
# The output is an error because the string "hello" cannot be converted to integers since it contains words.
# Convert the integer 12 to a float and multiply by 3.5. What is the result?
num_1 = 12
num_2 = 3.5
ANS_1 = float(num_1)*num_2
print(ANS_1)
# The result is a float.
# Convert 0 to a float. What is the type and value?
num_3 = 0
num_4 = float(0)
print(num_4, type(num_4))
# It is a float.
# Convert 7.89 into an integer. What is the result?
num_5 = 7.89
num_6 = int(num_5)
print(num_6)
# The result is 7, an integer.
# If x = 12.0, convert it to int. Does the value change?
x = 12.0
x_1 = int(12.0)
print(x_1, type(x_1))
# The value does not change.
# Convert the integer 100 to a string and concatenate it with " apples".
# Initiate a variable and assign it the value 100.
num_7 = 100
# Initiate another variable and use it to convert the integer to a string.
num_8 = str(100)
# The integer has been converted to a string.
ANS_3 = str(100) + " " + "apples"
print(ANS_3)
# What is the result of:
num = 45
print("Number: " + str(num))
# The result is a string.
# Convert "7.2" to a float and add 2.8. What is the result?
# Initiate a variable and assign is the string "7.2"
num_9 = "7.2"
# Initiate another variable and use it to convert the string to a float.
num_10 = float(num_9)
ANS_4 = num_10 + 2.8
# The result is a float.
# Convert "10" to float and multiply by 3. What is the output?
num_11 = "10"
num_12 = float(num_11)
ANS_5 = num_12*3
print(ANS_5)
# What is the boolean value of [] and [0]?
bool([])
# The result is False, the list contains nothing.
bool(0)
# The result is False, the number zero is nothing.
# Predict the result:
x = ""
y = bool(x)
print(y)
# The result is False.
# Convert 5 to boolean. What is the result?
bool(5)
# The result is True. The '5' is an integer.
# Using the table, convert 3.7 to integer and float. Show types.
# Initiate a variable and assign it the value'3.7'
num_13 = 3.7
# Initiate another variable and use it to convert '3.7' to an integer.
num_14 = int(num_13)
# Initiate another variable and use it to convert '3.7' to a float.
num_15 = float(num_13)
print(num_14, type(num_14))
print(num_15, type(num_15))
# Convert "0" to boolean. What is the result?
bool(0)
# The result is False, the number zero is nothing.
# Convert False to integer and float. Show outputs.
# Initiate a variable and assign it the value'False'
num_16 = False
# Initiate another variable and use it to convert 'False' to an integer.
num_17 = int(False)
# Initiate another variable and use it to convert 'False' to a float.
num_18 = float(False)
print(num_17)
print(num_18)
# The result will be an integer and a float.
# Ask the user for two numbers as input, convert them to integers, add them, and
# display the result.
# Initiate a variable for the user to input the first number.
num_19 = input("Type in a number")
# Initiate another variable for the user to input the second number.
num_20 = input("Type in another number")
# Convert both to integers.
num_21 = int(num_19)
num_22 = int(num_21)
ANS_6 = num_21 + num_22
print(ANS_6)
# Ask the user for their age as a string input, convert to integer, and print a message:
# You are <age> years old
# Initiate a variable for the user to input their age.
Age = input("How old are you?")
# Convert it to an integer.
AGE = int(Age)
Message = "You are" + " " + Age + " " + "years old!"
print(Message)
# Convert a float 12.75 to integer, string, and boolean. Print the value and type for
# each conversion.
# Initiate a variable for the number '12.75'.
num_23 = 12.75
num_24 = int(num_23)
# Converted to integer.
print(num_24, type(num_24))
num_25 = str(num_23)
# Converted to string.
print(num_25, type(num_25))
num_26 = bool(num_23)
# Converted to boolean.
print(num_26, type(num_26))
