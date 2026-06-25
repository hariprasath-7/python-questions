# create a list of 20 random integers between 1 and 10, generated using random library
import random 

l = []
for i in range(20):
    num = random.randint(1,10)
    l.append(num)
print(l)
# op:
# [6, 9, 3, 9, 9, 9, 9, 1, 8, 7, 3, 7, 2, 2, 10, 3, 10, 3, 6, 1]