# Indexing strings
# 0 1 2 3 4
# A P P L E


# Slicing
# 0 1 2
# A P P

word = "PYTHON"

# 0 1 2 3 4 5
# P Y T H O N

print(word[3], word[4], word[5])

sentence = "I am a boy, I live on Earth"
print(sentence[19],sentence[20])

# sentence is the variable name, dataType is string, value is "I am a boy, I live on Earth"
# [] accepts two arguments, first is the "Start point" while the second argument is the "End point".
# They are separated by a colun ":"
# These argument are strictly indexes, and integers.
print(sentence[0:10])

# Get the last charater in a string
print(sentence[-1:])
print(word[-1:])
print(word[-2:])

print("End point", word[:-1])

# -2 -1 0 1 2 3 4 5
#  0  N P Y T H O N


name = "John Doe"
firstInitials = name[0]
secondInitials = name[5]
print("Initials", firstInitials,secondInitials)    # prints first characters of first and last name
print(name[-8],name[-3])  # prints first characters of first and last name