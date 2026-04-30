#Find the maximum value in a list without using the built-in max() function.

numbers = [10, 24, 76, 34, 12]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)
