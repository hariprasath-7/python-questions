# create a python code to sort the list using while loop
# l=[9,3,7,1,6,3,4]

l = [9, 3, 7, 1, 6, 3, 4]
swapped = True

while swapped:
    swapped = False
    i = 0
    while i < len(l) - 1:
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
            swapped = True
        i += 1

print("Sorted list:", l)
