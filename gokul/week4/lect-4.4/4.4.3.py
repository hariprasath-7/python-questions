## Generate a list of 100 random numbers between 1 and 1000, and sort the list
##  create another list even, and add all the even numbers to this even list and print the list
## similarly create another list odd, and add all the odd numbers to this odd list and print the list
import random 
rl = []
el = []
ol = []

for i in range (100):
    n=random.randint(1,1000)
    rl.append(n)
rl.sort()
print(rl)

for num in rl :
    if num % 2 == 0:
        el.append(num)
    else:
        ol.append(num)

print("The even list",el)
print("The odd list",ol)