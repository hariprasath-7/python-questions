# Write a code to accept the string of length 10 from the user and print True if string has any character

# occurring 5 times consecutively in it, otherwise print False.
n = input ()
if len(n) == 10:
    if '#####' in n :
        print(True)
    else:
        print(False)
else:
    print("Error : The string length must be exactly 10")

# op:
# abcde#####
# True

