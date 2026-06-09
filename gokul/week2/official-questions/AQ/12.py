# Accept three integers as input from the user. Print good triplet if one of the three numbers is the sum of the other two, and bad triplet otherwise.
# code:
# x , y , z = int(input()),int(input()),int(input())

# if x + y == z :
#     print("gud triple")
# elif x + z == y :
#     print("gud triple")
# elif y + z == x:
#     print("gud triple")
# else:
#     print("bad triple")
#     # op:
# 1
# 2
# 3
# gud triple

# easy version 
x , y , z = int(input()),int(input()),int(input())

if x + y == z or x + z == y or y + z == x :
    print('Gud tripple ')
else:
    print("Bad triple ")

