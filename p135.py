#Take a list and return a new list with unique elements only

def remove_duplicates(data):
    return list(set(data))

print(remove_duplicates([1, 2, 2, 3, 4, 4]))
