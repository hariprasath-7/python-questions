# print(int(input()))

# predict the output for the below inputs

# INPUT 1 : -121
# INPUT 2 : abc
# INPUT 3 : 20.5


# n= -123456
# m=abs(n)
# print(str(m)==str(m)[::-1])

# op:
# INPUT 1 : -121 = True
# INPUT 2 : abc = error u cannot get absolute positive value of letters
# INPUT 3 : 20.5 = False 


num = int(input("Enter a number:"))

num_str = str(abs(num))
rev_str = ""

for ch in num_str:
    rev_str = ch + rev_str

if num_str == rev_str:
    print("palindrome")
else:
    print('Not a palindrome')

