# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# Add these two matrices and store it in C 
# op:
import numpy as np 

A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

B = np.array([
    [1,2,1],
    [6,2,3],
    [4,2,1]
])

C = A + B 
print(C)
# op:
# [[ 2  4  4] 
#  [10  7  9] 
#  [11 10 10]]