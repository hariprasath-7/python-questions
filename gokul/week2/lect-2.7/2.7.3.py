# predict the output


alpha="abcdefghijklmnopqrstuvwxyz"
i=24

print(alpha[i+1])
# print(alpha[i+2])
# print(alpha[i+2]%26)
print(alpha[(i+2)%26])
# op:
#  y
#  alpha[26] = not valid 
#  cant place a  square braced expression inside an paranthesis  
#  a 