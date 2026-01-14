temperature = 25

if temperature > 30:
    print("It's a hot day")
elif temperature < 20:
    print("It's a cold day")
else:
    print("It's a lovely day")

#-------------------------
x=10
y=5

print(x == y)
print(x != y)
print(x > y)

#------------------------

age = 16
print(f'age: {age}')

has_id = True

if age >= 18 and has_id:
    print("You are allowed to enter")
else:
    print("You are not allowed to enter")

is_student = True
is_senior = False

if is_student or is_senior:
    print("You get a discount")


#------------------------

is_logged_in = False

if not is_logged_in:
    print("Please log in to continue")

#------------------------

#check positive negative or zero

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

#------------------------
#simple grading system

score_str = input("Enter your score (0-100): ")
score = int(score_str)
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")   

#------------------------
# #is the year a leap year
# 
year_str = input("Enter a year: ")
year = int(year_str)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#------------------------ 
