# Write a program to print the Fibonacci series of n terms where n is always greater than or equal to 2.

# code:
n = int(input("Enter a number:"))

a = 0
b = 1

print(a)
print(b)

for i in range(n - 2):
    c = a + b
    print(c)
    a = b
    b = c
# op:
# Enter a number:6
# 0
# 1
# 1
# 2
# 3
# 5