#Two friends have sets of their favorite hobbies. Write a program to find which hobbies they both share.

friend_a = {"Hiking", "Reading", "Gaming", "Cooking"}
friend_b = {"Gaming", "Photography", "Cooking", "Running"}

common_hobbies = friend_a.intersection(friend_b)

print(common_hobbies)