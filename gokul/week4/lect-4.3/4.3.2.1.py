# will 10 be printed in the output? 
# what is the difference between range(1,10) and random.randint(1,10)
import random
for i in range(20):
    print(random.randint(1,10))
# op:
# 10 will be printed we are running the loop like 20 times and there is a lot of chances to print it multiple times
# range function runs without including the end value but random.randint will include the end value