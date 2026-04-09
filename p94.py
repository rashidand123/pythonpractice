#Find the largest number in a list [4, 12, 9, 30, 2].

nums = [4, 12, 9, 30, 2]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print("Largest:", largest)
