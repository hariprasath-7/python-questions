# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 

# B = 1 2 1
#     6 2 3
#     4 2 1 
# code:
import numpy as np 
A=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,6]
])

B=np.array([
    [1,2,2],
    [6,2,3],
    [4,2,1]
])
# unwanted :::
# result = A + B
# print(result)
# # # op:
# # [[ 2  4  5] 
# #  [10  7  9] 
# #  [11 10  7]]