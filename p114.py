# WAF to print the length of the list . (list is the parameter )

nums = [ "3","4","5","2","7","1"]
cities= [ "delhi", "gurgaon", "dehradun"]

def print_len(list):
    print(len(list))

print_len(nums)
print_len(cities)

#WAF to print the element of the list in a single line 

nums = [ "3","4","5","2","7","1"]
cities= [ "delhi", "gurgaon", "dehradun"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)        