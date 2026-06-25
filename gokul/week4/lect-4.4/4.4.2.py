## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
## findout the index of number 21 in the generated list, if the number is not present in the list print -1
import random 
l = []
for i in range(1000):
    n = random.randint(1,1000)
    l.append(n)
unique_numbers = set(l)
unique_list = list(unique_numbers)
unique_list.sort()
print(unique_list)
if 21 in unique_list :
    index_of_21 = unique_list.index(21)
    print("The index of 21 is ",index_of_21)
else:
    print("-1")
