
my_fruit_set = {"banana", "fig", "grapefruit"}

def check_for_fruit(fruit, fruit_set):
    if fruit in fruit_set:
        print("We have", fruit)
    else:
        print("We don't have", fruit)

check_for_fruit("fig", my_fruit_set)
check_for_fruit("apple", my_fruit_set)

my_fruit_set.add("apple") # use add to add item 
check_for_fruit("apple", my_fruit_set)
print(my_fruit_set)

my_fruit_set.remove("apple") # use remove item
check_for_fruit("apple", my_fruit_set)
my_veg_set = set() # construnct new empty set, cannot use {}., because it's dictionary, 
                   #if use {}, it should conclude at lease one element

print(set("spam"))