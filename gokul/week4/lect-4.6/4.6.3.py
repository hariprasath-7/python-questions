# write a piece of code to  find the dot product.

x=[1,7,3,4]
y=[8,6,3,2]
dot_prd = 0
for i in range(len(x)):
    dot_prd += x[i] * y[i]
print("The dot product of X and Y is :",dot_prd)