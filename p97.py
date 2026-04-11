#Write a Python program to find the length of a tuple without using the len() function.

my_tuple = (1, 2, 3, 4, 5)
count = 0
for _ in my_tuple:
    count += 1
print("Length =", count)