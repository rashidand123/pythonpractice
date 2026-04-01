# Creating a dictionary
student = {
    "name": "Drishti",
    "age": 20,
    "course": "BCA"
}

# Accessing values
print(student["name"])   # Drishti

# Adding a new key-value pair
student["city"] = "Meerut"

# Updating value
student["age"] = 21

# Removing an item
student.pop("course")

# Display dictionary
print(student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)