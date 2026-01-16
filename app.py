#For Loop

names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name) 


#------------------

for i in range(1,6):
    print(i)


#------------------

count = 0 

while count < 5:
    print("Count is:", count)
    count = count + 1

#------------------

numbers = [10, 20, 30, 40, 50]

x = 30

for num in numbers:
    print('checking', num)
    if num == x:
        print('Found', x)
        break
    print('Not found yet')


#------------------

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in number_list:
    if num == 5:
        continue
    print(num)

#------------------

numbers_list = [10, 20, 30, 40, 50]

for num in numbers_list:
    print(num)

#------------------

string = "Hello, World!"

for char in string:
    if char == ',' or char == ' ' :
        continue
    print(char)

#------------------

for i in range(1, 11):
    print(i)

#------------------

my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(key)

for key, value in my_dict.items():
    print(key, value)

#------------------

count = 0 

while count <5:
    print("Count is:", count)
    count += 1

#------------------

correct_password = "secure123"
attempt = 0
max_attempts = 3

# while attempt < max_attempts:
#     user_input = input("Enter password: ")
#     if user_input == correct_password:
#         print("Access granted")
#         break
#     if attempt == max_attempts - 1:
#         print("Access denied")
#         break
#     else:
#         print("Incorrect password")
#         attempt += 1


#------------------

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in number_list:
    if num == 7:
        print("found 7, stopping the loop")
        break
    print(num)


for num in number_list:
    if num % 2 == 0:
        continue
    print(num)

#------------------

num = [10,-5,2,-1,8,-3]
sum =0 

for n in num:
    if n % 2 ==0:
        sum += n
        print("sum so far:", sum)
    else:
        continue
