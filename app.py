my_string = "hello, python coders"

print(my_string[0:5:3])
print(my_string[::-1])


#len()
print(len(my_string))

#case conversion
print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())
print(my_string.title())
print(my_string.swapcase())

#finding substrings
print(my_string.find("python"))
print(type(my_string.find("potato")))   

#replacing substrings
bad_string = "hello, potato coders"
good_string = bad_string.replace("potato", "python")
print(good_string)

terrible_string = "hello potato potato potato coders"
better_string = terrible_string.replace("potato", "python", 2)
print(better_string)

#removing whitespace
whitespace_string = "   hello, python coders    "
print(whitespace_string.strip())
print(whitespace_string.lstrip())
print(whitespace_string.rstrip())

dotted_string = "...hello, python coders..."
print(dotted_string.strip("."))
print(dotted_string.lstrip("."))
print(dotted_string.rstrip("."))

#checking prefixes and suffixes
file_name = "document.pdf"
print(file_name.endswith(".pdf"))
print(file_name.startswith("doc"))
print(file_name.startswith("pdf"))

#practice exercise

input_string = input("Enter a string: ")
input_string = str(input_string)

if not input_string:
    print('No string entered')
    exit()


#convert to lowercase
processed_input_string = input_string.strip()
processed_input_string = processed_input_string.lower()

length = len(processed_input_string)

python_present = processed_input_string.find("python")
if python_present != -1:
    print(f'The string contains "python"')

processed_input_string = processed_input_string.replace("python", "PYTHON")


########################
print('############################')

input_words = input("Enter word: ")

input_words = input_words.lower()

input_word_backwards = input_words[::-1]

if input_words == input_word_backwards:
    print("The word is a palindrome")
