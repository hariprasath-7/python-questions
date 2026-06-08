# write a python code where you will take an input number k and a string s.
# you have to move the string by k characters to the right

# TestCase 1
'''
INPUT:
    s='abcdefg'
    k=2

OUTPUT: 'cdefghi`
'''

# TestCase 2
'''
INPUT:
    s='chennai'
    k=20
OUTPUT:
    'wbyhhuc'
'''
# op:
alpha = "abcdefghijklmnopqrstuvwxyz"
s = input()
k = int(input())
result = " "

for ch in s :
    pos = alpha.index(ch)
    new_pos = (pos + k) % 26
    result +=alpha[new_pos]

print (result)

