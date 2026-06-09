# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not


# # HINT : subtract current year from YOB
year = int(input("Enter ur YOB:"))
age = (2026-year)
print(age)
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# from datetime import datetime
# current_year = datetime.now().year
# y = int(input("Enter the YOB"))
# age=current_year-year
# x = ? age>=18 'Eligibile to Vote'  : 'Not Eligible'
# print(x)

