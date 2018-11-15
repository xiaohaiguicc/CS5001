import random as rnd

num = rnd.random()
print("Random number between 0.0 and 1.0", num)

num = rnd.randint(5,25)#random.randint(a,b) return a random integer N between a and b
print("Random number between 5 and 25", num)

my_string = "Hello Wolrd"
print("A random character picked from",my_string,rnd.choice(my_string))#random.choice(seq),return a random element.

print(rnd.choice(['red,yellow,blue,green','1','2','3']))
