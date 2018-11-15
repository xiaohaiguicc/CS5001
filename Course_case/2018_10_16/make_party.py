from person import Person


def main():
    p1 = Person("aaa", 38)
    p1.introduce_self()

    p2 = Person("bbb", 22)
    p2.introduce_self()
    p2.say_hello()

    p3 = Person("ccc", 21)
    p4 = Person("ddd", 15)
    
    p4.befriend(p2)
    p4.befriend(p1)
    p4.befriend(Person("eee", 88))

    p4.introduce_self()




main()
