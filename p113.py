#functions in python
#built in functions

print("hello","world")
print("hello")
print("world")
print("hello", end=" ")
print("world")

#Default parameters
def cal_prod(a=1,b=1):
    print(a*b)
    return a*b 

cal_prod()
#
def cal_prod(a,b=2):
    print(a*b)
    return a*b 

cal_prod(1)