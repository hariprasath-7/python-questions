# Write a code to accept a string as input and determine if it is a palindrome or not.
n = input()
rev_str = ""
for ch in n :
    rev_str = ch + rev_str

if n == rev_str :
    print("palindrome")
else:
    print("not a palindrome")

# op:
# 1221
# palindrome