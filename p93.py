#Find the factorial of a number (e.g., 5! = 120).

num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)