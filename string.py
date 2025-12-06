# type: ignore

# (1) Indexing
text = "TABLE"

# Access the first character
print(text[0])

# Access the last character
print(text[-1])

# T A B L E
# 0 1 2 3 4

# (2) String Slicing
# string[start:end]
print(text[0:3])  # TAB
print(text[1:])   # ABLE
print(text[1:5])  # ABLE

# (3) Immutability
new_text = "HELLO"

# Modify HELLO to YELLO
copy_of_new_text = "Y" + new_text[1:]
print(copy_of_new_text)

# (4) Escaping Characters
# Using quotes inside a string

# She said, "Hello!"
print("She said, \"Hello!\"")

# This is a blakslash: \
print("This is a blackslash: \\")

# (5) Creating a new line
# \n
print("1. Blue \n2. Orange")

# (6) Creating Tabline
# \t
print("Name:\tAustine")