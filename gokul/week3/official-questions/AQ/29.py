# Write a program to print the first and last digits of a number without converting it to string.
num = int(input())

last_digit = num % 10

first_digit = num
while first_digit >= 10:
    first_digit = first_digit // 10

print(first_digit)
print(last_digit)
