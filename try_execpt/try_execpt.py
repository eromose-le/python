# A program to collect integer as input from a user

try:
  number = int(input("Enter a number: "))
except ValueError:
  print("Oops! That's not a valid number.")

