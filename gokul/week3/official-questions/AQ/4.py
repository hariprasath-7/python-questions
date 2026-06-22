# Write a program to accept the positive integer n from the user and print counting of numbers which are not

# prime from 1 to n.
n = abs(int(input("enter a number:")))
not_prime_count = 0
for num in range (1, n + 1 ):
    if num <= 1:
        not_prime_count = not_prime_count + 1
    else:
        for i in range (2,num):
            if num % i == 0:
                not_prime_count = not_prime_count + 1 
                break
print(not_prime_count)

# op:
# enter a number:5
# 2


