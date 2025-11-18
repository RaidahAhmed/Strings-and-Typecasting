# Print the first and last character of "Programming".
Word = "Programming"
print(Word[0])
# The index '0' is where 'P' is located.
print(Word[10])
# The index '10' is where 'g' is located.
# Extract the substring "gram" from "Programming" using slicing.
word = "Programming"
print(word[3: 7])
# The index '3' is where the substring starts and the index '7' is where it ends.
# Reverse the string "Python" using slicing.
s = "Python"
print(s[::-1])
# Concatenate "Python" and "Rocks" with a space in between.
WORD_1 = "Python"
WORD_2 = "Rocks"
Final_word = WORD_1 + " " + WORD_2
# This adds the two words together with " " representing a space in between.
print(Final_word)
# Combine "Data" and "Science" into a single string.
WORD_3 = "Data"
WORD_4 = "Science"
Final = WORD_3 + "" + WORD_4
# This adds the two words together without a space in between.
print(Final)
# Print your name and age using f-strings.
# Initiate two variables and give them values.
Name = "Raidah"
age = 21
print(f"My name is {Name} and I am {age} years old.")
# The 'f' enables us to insert a variable in a string.
# Use format() to print "I love Python" with a variable storing "Python".
# Initiate a variable to store the word "Python".
WORD_5 = "Python"
# Use the ".format()" to insert the variable into the string.
print("I love {}".format(WORD_5))
# Use % formatting to display "Score: 95%" with a variable score = 95.
score = 95
# Use the '%' formatter to insert the variable.
print("Score:%s" % score)
# Convert "python" to "PYTHON".
"python".upper()
# Converts the word to upper case using the '.upper()' method.
# Remove extra spaces from " Data Science ".
" Data Science ".strip()
# Removes the outer spaces using the 'strip()' method.
# Replace "Java" with "Python" in "I love Java".
"I love Java".replace("Python", "Java")
# Replaces the word using 'replace("new", "old")' method.
# Split "apple,banana,cherry" into a list.
"apple,banana,cherry".split(",")
# Splits the string into a list by the commas.
# Join ["Python", "is", "fun"] with spaces to form a sentence.
" ".join(["Python", "is", "fun"])
# Joins the list back into one string with spaces in between.
# Print "Hello" and "Python" on two separate lines.
print("Hello\nPython")
# The escape character '\n' prints the second word on a new line.
# Print a path "C:\newfolder\test" correctly using escape characters.
path = r"C:\newfolder\test"
print(path)
# Prints a file path using the 'r' string.
# Change "Python" to "Pyxhon" by creating a new string.
# Initiate a new variable and store "Python" in it.
s = "Python"
# Initiate another variable and replace 't' with 'x' in it.
new_s = s[0:2] + "x" + s[3:6]
print(new_s)
# Try changing a character directly and note the error.
r = "Raidah"
r[0] = "Q"
# TypeError: 'str' object does not support item assignment.
