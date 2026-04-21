#Write a program that takes an integer input from the user and prints whether it is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
