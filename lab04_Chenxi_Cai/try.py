

x = 2
def A():
    x = 5
    def B():
        print(x)
    B()

A()