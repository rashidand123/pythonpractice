#conditional statements
marks=int(input("enter student marks"))

if marks >= 90:
  grade = "A"
elif marks >= 80:
  grade = "B"
elif marks >= 70:
  grade = "C"
else:
  grade = "D"

print(grade)
