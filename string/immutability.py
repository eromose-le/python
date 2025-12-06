# Change or Modify String

# This would not work, as you can't directly modify a string.
# name = "Christopher"
# name[0] = "I"


# name = "Christopher_junior" # Christopher Junior
# new_name = "T" + name[1:]
# print(new_name)

name = "Christopher"
new_name = "T" + name[1:]
print(id(name))
print(id(new_name))

