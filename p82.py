#write a program to enter marks of 3 subjects from the user and store them in a dictionary. 
#start with an empty dictionary and add one by one .Use subject name as key and marks as value

marks={}

x=int(input("enter phy: "))
marks.update({"phy": x})

x=int(input("enter math: "))
marks.update({"math": x})

x=int(input("enter chem : "))
marks.update({"chem": x})

print(marks)

#figure out a way to store 9 & 9.0 as seperate values in the set.(you can take a help of built - in -types)


values={9, 9.0}
print(values)

values={
    ("float", 9.0),
    ("int", 9)
}
print(values)