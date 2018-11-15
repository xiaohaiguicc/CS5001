
band = ["Paul","Prter","Ana","Boss"]
print(band)
print(band[1])
band[1] = "Bob"
print(band)

#zip function 
instruments = ["Bass","Violin","Paino","Guitar"]
lineup = list(zip(band, instruments))#return a combined list

for band_memeber in lineup:
    print("Band member:", band_memeber)

#list index
fruits = ["Apple","Banana","peach","pineapple","lemon","pear"]
print(fruits[:5])

#use "for" 
first_letters = [fruit_string[0] for fruit_string in fruits ] #list comprehension
print(first_letters)

string = "I'm here, I'm a string."
number_characters = [number_char for number_char in zip(range(len(string)),string)]#string is a list of chars.
print(number_characters)

#list in list
lists_of_lists = [["Apple","Banana","peach","pineapple"],[1,2,3,4,5],["Bass","Violin","Paino","Guitar"]]
print(lists_of_lists[1])
print(lists_of_lists[2][2]) # third list's third element.

#represent a string in list format
str_list = list("Hello")
print(str_list)

#split
fruit_string = "Apple, Banana, peach, pineapple"
fruit_string = fruit_string.split(", ")
for fruit in fruit_string:
    print("This is fruit:", fruit)

#ASCII transformation
input_string = input("Please enter a string:")
char_pairs = [(char,ord(char)) for char in input_string ] #a tuple.
for char_pair in char_pairs:
    print(char_pair) 