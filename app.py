#Lists

my_mixed_list = [42, "hello", 3.14, True, "world", 7]

my_list = ["apple", "banana", "cherry", "date"]

empty_list = []

numbers = [1, 2, 3, 4, 5]

list_from_string = "hello"

list_from_string = list(list_from_string) 

######

first_fruit = my_list[0]  # "apple"
second_fruit = my_list[1]  # "banana"
last_fruit = my_list[-1]  # "date"
second_last_fruit = my_list[-2]  # "cherry"

print(first_fruit, second_fruit, last_fruit, second_last_fruit)

##########################################################
fruits_slice = my_list[1:4:2]  # ["banana", "cherry", "date"]
print(fruits_slice)

fruits_to_end = my_list[2:]  # ["cherry", "date"]
print(fruits_to_end)

fruits_from_start = my_list[:3]  # ["apple", "banana", "cherry"]
print(fruits_from_start)
##########################################################
list_length = len(my_list)  # 4
print(list_length)


##########################################################
my_list.append("elderberry")
print(my_list)  # ["apple", "banana", "cherry", "date", "elderberry"]
my_list.insert(1, "blueberry")
print(my_list)  # ["apple", "blueberry", "banana", "cherry", "date", "elderberry"]
my_list.remove("cherry")

##########################################################
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

combined_list = list_1  +  list_2  # [1, 2, 3, 4, 5, 6]
print(combined_list)

printed_list = list_1 * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
#print(printed_list)

is_2_in_list = 2 in list_1  # True
is_5_not_in_list = 5 not in list_1  # True
print(is_2_in_list, is_5_not_in_list)

###########################################################

