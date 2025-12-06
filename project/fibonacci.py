# 0 1 1 2 3 5
def fibonacci(n):
    if n <= 1:
        return n
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return n

# numbers = [0, 1, 2, 3, 4, 5]
# range(6) = 0, 1, 2, 3, 4, 5
for i in range(6):
    print(f"Fibonacci at position {i} is {fibonacci(i)}")

# 1. Function: fibonacci(n) gives the number at position n in the Fibonacci sequence.

# 2. If the number is 0 or 1, we already know what it is (it returns 0 or 1).

# 3. If it’s more than 1, it adds the two numbers before it — that’s how Fibonacci works!

# 4. Loop: It runs the function for positions 0, 1, and 2 using range(3).


# 0, 1, 0+1=1, 1+1=2, 1+2=3
# Fibonacci(n)    ----- ??
# 1. Fibonacci(0) ----- 0
# 2. Fibonacci(1) ----- 0, 1
# 3. Fibonacci(2) ----- (2-1=1) + (2-2=0) = 1  <----->  (n-2) + (n-1) = n
