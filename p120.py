#Calculate the factorial of a number (e.g., 5! = 5 × 4 × 3 × 2 × 1).

 def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5 is: {factorial(5)}")
