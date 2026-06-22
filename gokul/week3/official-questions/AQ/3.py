# Write a program to accept the positive integer n from the user and print the average of all number's factorial

# from 1 to n .
n = int(input("enter a number:"))
total_sum = 0
fact = 1
for i in range(1,n + 1):
    fact = fact * i
    total_sum = total_sum + fact 
average = total_sum / n
# print("Factorial",fact)
# print("Sum of total",total_sum)
print("Average",average)

