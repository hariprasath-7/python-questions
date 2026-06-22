# Write a program to accept the string s from the user and print all alphabets in one line separated by , before

# first occurrence of vowels .
# code:
s = input()
output_letters = []

for ch in s:
    if ch.lower() in 'aeiou':
        break

    if ch.isalpha():
        output_letters.append(ch)
print(",".join(output_letters))