 # What is the difference between the string methods find and index ?

# Ans:
# Use find() if you are not sure the item is there. It is safer because it will not crash your code.
# Use index() if you expect the item to be there and want your program to flag an error if it goes missing.

# label = input("Enter column label: ").upper()

# # Check if the label is just 1 letter
# if len(label) == 1:
#     column_number = ord(label[0]) - ord('A') + 1

# # Check if the label has 2 letters
# elif len(label) == 2:
#     first_val = ord(label[0]) - ord('A') + 1
#     second_val = ord(label[1]) - ord('A') + 1
    
#     # First letter counts for 26 units each
#     column_number = (first_val * 26) + second_val

# print("Output:", column_number)


print("When did India get independance (year)?")
year = int(input())

while (year !=1947):
    print("you got this wrong. Enter once again.")
    year = int(input())
print("Wowwwww... you got it right!1940")
