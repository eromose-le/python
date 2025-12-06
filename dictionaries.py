student = {
  "name": "Chimadika",
  "age": 12,
  "best_color": "blue"
}

# Add
student["height"] = "163cm"

# Remove
del student["best_color"];

# print(student["height"])
# print(student)

if "name" in student:
  print("name exists")
else:
  print("key not found!")

student = {}
print(student)