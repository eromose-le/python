# if statement example
number = int(input("Enter a Number = "))

if 10 != number:
    print("10 not equal ", number)
elif 10 > number:
    print("10 greater than ", number)
elif 10 == number:
    print("10 equal to ", number)
else:
    print("10 less than ", number)

print("Program ended")