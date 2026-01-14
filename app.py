num1 = 25
num2 = 7

print("arithmetic operations")
sum_result = num1 + num2
print(f'Sum: {sum_result}')
difference_result = num1 - num2
print(f'Difference: {difference_result}')
product_result = num1 * num2
print(f'Product: {product_result}')
division_float_result = num1 / num2
print(f'Division (float): {division_float_result}')
division_int_result = num1 // num2
print(f'Division (int): {division_int_result}')
modulus_result = num1 % num2
print(f'Modulus: {modulus_result}')
exponentiation_result = num1 ** num2
print(f'Exponentiation: {exponentiation_result}')


BIDMAS_result = num1 + num2 * 2
print(f'BIDMAS Result (num1 + num2 * 2): {BIDMAS_result}')
BIDMAS_result_parentheses = (num1 + num2) * 2
print(f'BIDMAS Result with Parentheses ((num1 + num2) * 2): {BIDMAS_result_parentheses}')

#--- Comparison Operations ---
print("\ncomparison operations")

age = 20

is_exaactly_20 = (age == 20)
print(f'Is age exactly 20? {is_exaactly_20}')

is_age_not_20 = (age != 20)
print(f'Is age not 20? {is_age_not_20}')    

is_age_greater_than_18 = (age > 18)
print(f'Is age greater than 18? {is_age_greater_than_18}')

is_age_less_than_18 = (age < 18)
print(f'Is age less than 18? {is_age_less_than_18}')

is_age_greater_equal_18 = (age >= 18)  
print(f'Is age greater than or equal to 18? {is_age_greater_equal_18}')

is_age_less_equal_18 = (age <= 18)
print(f'Is age less than or equal to 18? {is_age_less_equal_18}')

print("--------------------------------")

print("is 10 = 10 ?", 10 == 10)

print("is apple = orange ?", "apple" == "orange")

print(f'is apple = Apple ?',"apple" == "Apple")

#-------------
#BMI CALCULATOR
print("\nBMI CALCULATOR")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
bmi_rounded = round(bmi, 2)
print(f'Your BMI is: {bmi_rounded}')

healthy_bmi = 18.5 <= bmi <= 24.9
unhealthy_bmi = bmi < 18.5 or bmi > 24.9

print(f'Is your BMI in the healthy range (18.5 - 24.9)? {healthy_bmi}')

#-------------------------------

rectangle_length = float(input("\nEnter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))
area = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {area}')

is_area_greater_than_100 = area > 100
print(f'Is the area greater than 100? {is_area_greater_than_100}')
