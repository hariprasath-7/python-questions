
# write a python script for the below test case,
# Note the input will be of 5 characters long,


# testcase 1
'''
INPUT : 'gokul'
OUTPUT : 'hplvm'
'''

# testcase 2
'''
INPUT: 'abcde'
OUTPUT: 'bcdef'
'''

# solution:
IN = 'gokul'
OUT = ''
for i in IN :
    i = ord(i)
    i +=1
    OUT += chr(i)
print(OUT)
    
