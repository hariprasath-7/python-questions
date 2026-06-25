## generate a list of 15 numbers random numbers from 1 to 15 and sort it
## print all the numbers from 1 to 15 , which are not in the generated list
import random 
l =[]
for i in range (15):
    n = random.randint(1,15)
    l.append(n)
l.sort()
print(l)
print("The numbers not in generated list are")
for num in range(1,16):
    if num not in l:
        print(num)
# op:
# [1, 1, 4, 5, 7, 7, 8, 8, 9, 10, 11, 11, 12, 12, 14]
# The numbers not in generated list are
# 2
# 3
# 6
# 13
# 15