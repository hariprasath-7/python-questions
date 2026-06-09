# On what day of the week were you born? If you don't know the answer to this, use the calendar library to get the answer.
# code:


import calendar 

year = 2006
month = 1
date = 13 

print(calendar.day_name[calendar.weekday(year,month,date)])
# op:
# Friday