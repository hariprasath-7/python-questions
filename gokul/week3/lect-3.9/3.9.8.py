# what will be the output of the below code?
# for i in range(5):
#     print(i, end=' ')
    
# for i in range(5):
#     print(i, a=' ')
    

# for i in range(5):
#     print(i, end=3)
    

#op:
# 1 2 3 4 
# error
# error 

num = int(input("Enter a number:"))
num_str = str(abs(num))
rev_str =''

for ch in num_str :
    rev_str=ch + rev_str

rev = int(rev_str)

if num <0 :
    ptint(-rev)
else:
    print(rev)