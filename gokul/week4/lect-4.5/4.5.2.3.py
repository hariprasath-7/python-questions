# what will be the output?Explain the output.

l=[1,5,2,9,3,6]
m=[9,2,1,7,3,0]
sorted(l)
print(l)
m.sort()
print(m)
# ANS:
# the soretd(l) makes a new copy of the list but not stored in any variable so print(l) prints the untouced variable l 
# the m.sort() sort the list and not created a new list and when we print it give the sorted value of the list 