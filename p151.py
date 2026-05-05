# Combine two dictionaries into one. If there are overlapping keys, the second dictionary's value should prevail.

dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}
dict1.update(dict2)
print(dict1)