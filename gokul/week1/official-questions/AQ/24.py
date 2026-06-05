# Accept a two digit number as input and print the sum of its digits. What about a three digit number?
num = int(input())

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

print(hundreds + tens + ones)
