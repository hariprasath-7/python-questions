# Accept three non-negative real numbers as input from the user. If the three numbers form the sides of a triangle, print True . If not, print False.

# code:

x , y ,z= float(input()),float(input()),float(input())

if x + y > z and x + z > y and y + z > x :
    print("True")
else:
    print("false")

# op:
# 3
# 4
# 5
# True

# 1
# 2
# 3
# false