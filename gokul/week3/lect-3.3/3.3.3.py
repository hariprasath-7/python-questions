# find the factorial of a number using while loop, take number n as input

# code:

n = int(input("Enter a number: "))

factorial = 1

counter = n

while counter > 0:
    factorial = factorial * counter
    counter = counter - 1  

print("The factorial is:", factorial)

# op:
# Enter a number : 6
# The factorial is : 720


