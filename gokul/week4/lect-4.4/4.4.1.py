## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
# after sorting, print the smallest, second smallest, largest and second largest number in the list
import random 
l = []
for i in range(1000):
    num = random.randint(1,1000)
    l.append(num)
unique_numbers = set(l)
unique_list = list(unique_numbers)
unique_list.sort()
print("The full lsit",unique_list)
print("Smallest",unique_list[0])
print("The second smallest:",unique_list[1])
print("Largest",unique_list[-1])
print("The second largest:",unique_list[-2])
# op:
# Smallest 3
# The second smallest: 4
# Largest 999
# The second largest: 998