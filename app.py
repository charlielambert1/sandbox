#mutable lists
fruits = ["apple", "banana", "cherry"]
print(fruits)

print_first_item = fruits[0]
print("First fruit:", print_first_item)
print_last_item = fruits[-1]
print("Last fruit:", print_last_item)

#####################
fruits[1] = "blueberry"
print("Updated fruits:", fruits)
#####################
fruits.append("date")
print("Fruits after appending date:", fruits)

fruits.append("blueberry")
print("Fruits after appending blueberry again:", fruits)
#####################
fruits = ["apple", "blueberry", "cherry", "date"]
fruits.insert(1, "banana")
print("Fruits after inserting banana at index 1:", fruits)

fruits.insert(0,"kiwi")
print("Fruits after inserting kiwi at index 0:", fruits)   
#####################

fruits.remove("banana")
print("Fruits after removing banana:", fruits)

if "grape" in fruits:
    fruits.remove("grape")

#####################
print("Fruits before popping the last item:", fruits)
item_removed = fruits.pop(0)
print("Fruits after popping the last item:", fruits)
print("Item removed:", item_removed)
#####################

fruits = ["apple", "banana", "cherry", "date"]
del fruits[2]
print("Fruits after deleting item at index 2:", fruits)
#####################

print("Fruits before deleting a slice:", fruits)
del fruits[1:2]
print("Fruits after deleting a slice:", fruits)

#####################

fruits.clear()
print("Fruits after clearing all items:", fruits)