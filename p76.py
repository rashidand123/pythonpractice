#Sets method
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("hello")

collection.remove(1)
collection.clear()
print(len(collection))

collection = {"hello", "world", "coding","python"}

print(collection.pop())
print(collection.pop())

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1.intersection(set2))