#Combine two dictionaries into one. If keys overlap, the second dictionary's value should prevail.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Using the merge operator (Python 3.9+)
merged = dict1 | dict2
print(merged)
