# 0 1 1 2 3 5
def fibonacci(n):
    if n <= 1:
        return n
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return n

try:
    count = int(input("Input number of sequence: "))
    
    for i in range(count):
        print(f"Fibonacci at position {i} is {fibonacci(i)}")

except ValueError:
    print("Error Occured: Invalid input, try again!")


