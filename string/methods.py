# Methods in Python Strings

name = "Austine+   "
stripped_name = name.strip()                          # Strip method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
replaced_name = stripped_name.replace("+", "")        # Replace method replaces a string with another string
capitalized_name = replaced_name.upper()              # Upper method converts all lowercase characters in a string into uppercase characters
lower_cap_name = capitalized_name.lower()             # Lower method converts all uppercase characters in a string into lowercase characters
reversed_name = lower_cap_name[::-1]                  # Reversing a string using slicing
count_of_substring = reversed_name.count("a")         # Count method counts the number of occurrences of a substring in a string
find_index_of_substring = reversed_name.find("t")     # Find method finds the first occurrence of a substring in a string and returns its index



print("Stripped name :-", stripped_name)
print("Replaced name :-", replaced_name)
print("Capitalized name :-", capitalized_name)
print("Lower cap name :-", lower_cap_name)
print("Reversed lower_cap_name :-", reversed_name)
print("Count of 'a' in reversed_name :-", count_of_substring)
print("Index of 't' in reversed_name :-", find_index_of_substring)