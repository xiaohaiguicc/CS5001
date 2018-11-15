my_fruit_counter = {}
my_fruit_counter["banana"] = 5
my_fruit_counter["orange"] = 10
my_fruit_counter["apple"] = 3
my_fruit_counter["fig"] = 1
#Any immutable can be key, value can be immutable or mutable

if "apple" in my_fruit_counter: # can use "in" to find keys
    print("yes")

print(my_fruit_counter[:2])
for fruit in my_fruit_counter:
    print(fruit) #print keys 而不是pair 和 
    # for key in my_fruit_counter.keys():
#     print(key) 一样

print(my_fruit_counter.keys())# print keys as a list
print(my_fruit_counter.values())# print values as a list
print(my_fruit_counter.items())# print (key, value) pair as a list
print(sorted(my_fruit_counter.items())) # 根据key排列item后输出(default ordering), can change ordering rule with second attribute. see below

fruits_by_count = sorted( #sorted 返回list with item tuple [(key: value)]
    my_fruit_counter.items(), 
    key=lambda x: x[1],
    reverse=True) # lambda is like a function,指的是根据value排， reverse means 根据value从大到小排
print(fruits_by_count)

# use dict and zip to combine two lists and become a dictionary
names = ['Fred', 'Ella', 'Owen', 'Zoe']
numbers = [4174, 2287, 5003, 2012]
d = dict(zip(names, numbers))


# my_food_type = {
#     "vegetables": [], #can also be dictionary in a dictionary
#     "meat": [],
#     "fruits": []
# }
# my_food_type["vegetables"].append("celery")
# my_food_type["vegetables"].append("carrot")
# my_food_type["vegetables"].append("zucchini")

# for food in my_food_type["vegetables"]:
    # print(food)

    