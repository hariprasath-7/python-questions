# write a code to find whether the given number is prime or not
# num = int(input("enter a numbre:"))
# is_prime = True 

# if num <=1 :
#     is_prime = False
# else:
#     for i in range (2,num):
#         if num % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print("is a prime")
# else:
#     print("is not a prime ")

# op:
# enter a numbre:5
# is a prime

# enter a numbre:6
# is not a prime 


words = input().split()
max_length = 0 


for current_word in words :
    if current_word == "-1":
        break

    word_len = len(current_word)

    if word_len > max_length :
        max_length = word_len
print(max_length)