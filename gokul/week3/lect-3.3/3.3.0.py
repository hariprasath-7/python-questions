# take a string as input and print it back by removing the first and last character of the input string
# code:

# user_string = input("Enter a string:")

# if len(user_string) >= 2:
#     modified_str=user_string[1:-1]
#     print(modified_str)
# else:
#     print("")

# op:
# Enter a string:APPLE
# PPL

n = input("Enter a number:")

if n.startswith('-'):
    clean_n = n[1]
else:
    clean_n = n


if clean_n  == clean_n[::-1] :
    print("palindrome")
else:
    print("not a palindrome")