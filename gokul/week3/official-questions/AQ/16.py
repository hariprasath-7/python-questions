# Write a code to accept the name of a person as input and print the initials as output. Assume that the name will be of this form: <first name> <last name> . Also assume that the first name and last name will be a single word, and there will be exactly one space between the two

# names. For example, if the input is Rohit Sharma, the output should be RS.
# code:
# name = input("enter ur name:")
# name_split = name.split()
# fi = name_split[0][0].upper()
# li = name_split[1][0].upper()
# print(fi + li)
# # op:
# enter ur name:hari prasath 
# HP
def count_boxes(sequence):
    total_bars = sequence.count('|')
    egg_boxes = sequence.count('0')
    
    total_boxes = total_bars - 1
    empty_boxes = total_boxes - egg_boxes
    
    return {
        "total_boxes": total_boxes,
        "empty_boxes": empty_boxes,
        "egg_boxes": egg_boxes
    }

sequence = "|0||0|||0|"
results = count_boxes(sequence)

print(f"Total number of boxes: {results['total_boxes']}")
print(f"Number of empty boxes: {results['empty_boxes']}")
print(f"Number of boxes that have eggs in them: {results['egg_boxes']}")
