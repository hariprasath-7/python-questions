# Two numbers n1 and n2 are said to be the same if they have an equal number of digits in them. Write a program to check whether n1 and n2 are the same. n1 and n2 are positive integers entered by the user without converting the number to string.

n1 = int(input())
n2 = int(input())

count1 = 0
temp1 = n1
while temp1 > 0:
    count1 += 1
    temp1 = temp1 // 10

count2 = 0
temp2 = n2
while temp2 > 0:
    count2 += 1
    temp2 = temp2 // 10

if count1 == count2:
    print("Same")
else:
    print("Not Same")
