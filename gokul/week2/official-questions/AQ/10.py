# Problem-10:

# Accept an integer x as input from the user. If the number is even, print even . If the number is odd, print odd.
# # code:
# if int( input("enter the number:")) % 2 == 0 :
#     print("even")
# else :
#     print("odd")

# op:
# enter a number : 6
# even 



x = int (input("enter a number :"))
last_num = x % 10 

words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]

print(words[last_num])


 