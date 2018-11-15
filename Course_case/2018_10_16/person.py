class Person: # Capital letter
    """A class representing a person"""
    # write a constructor
    def __init__(self, name, age):
        """Constructor for Person"""
        self.name = name
        self.age = age
        self.friend = []

    def introduce_self(self):
        """person self introduction"""
        print("Hi, I'm", self.name, "and I'm", self.age, "years old")
        if len(self.friend) > 0:
            self.introduce_friend()
        print()
    
    def say_hello(self):
        print("Hello")
    
    def befriend(self, new_friend): 
        # new_firend is a Person object
        print("be friend", new_friend.name)
        self.add_friend(new_friend)
        new_friend.add_friend(self)
        #new_friend.befriend(self)  #it is a recursion error,

    def add_friend(self, new_friend):
        self.friend.append(new_friend)


    def introduce_friend(self):
        print("\tFriends are:")
        for friend in self.friend:
            print("\t\t" + friend.name) # Assume friend is a Person object