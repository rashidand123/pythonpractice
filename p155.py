# Since tuples are immutable, you cannot change them directly. Change the value 20 to 25 in the tuple (10, 20, 30) by converting it to a list first.


tup = (10, 20, 30)
temp_list = list(tup)
temp_list[1] = 25
tup = tuple(temp_list)
print(tup)  