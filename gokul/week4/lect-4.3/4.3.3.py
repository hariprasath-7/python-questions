# create a list of 20 random integers between 1 and 10, generated using random library, and sort the list
import random 
l =[]
for i in range(20):
    num = random.randint(1,10)
    l.append(num)
l.sort()
print(l)
# op:
# [1, 2, 2, 2, 2, 2, 3, 5, 5, 5, 7, 8, 8, 8, 9, 10, 10, 10, 10, 10]