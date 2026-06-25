## write a python code to print the minimum element of the list, using for loop

l=[1,44,22,11,23,36,49,28,31,8,54,54]


min_val = l[0]
for num in l:
    if num < min_val :
        min_val= num 
print("The smallest number in the list is ",min_val)
