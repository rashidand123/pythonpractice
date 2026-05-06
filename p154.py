# Find the largest number in a list without using the built-in max() function.

def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_max([10, 5, 20, 8]))