from queue_list import Queue1


coffee_queue = Queue1()

while True:
    to_do = input("What do you want to do?\n")
    if to_do == "order":
        name = input("What's your name?\n")
        coffee_queue.enqueue(name)
    elif to_do == "collect":
        if not coffee_queue.is_empty():
            print("Coffee is ready for", coffee_queue.dequeue())
        else:
            print("No moew orders coming.")
    elif to_do == "check queue":
        print(coffee_queue) # print object will print out the memory location. print out how the object is represented as a string