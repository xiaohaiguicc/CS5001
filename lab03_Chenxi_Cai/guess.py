import random as rnd
import math
#Number guessing game deluxe

def guess(diff):
    if(diff <= 1):
        num_guess = int(input("Your guess is scalding hot\n"))
    elif(diff <= 2):
        num_guess = int(input("Your guess is extremely warm\n"))
    elif(diff <= 3):
        num_guess = int(input("Your guess is very warm\n"))
    elif(diff <= 5):
        num_guess = int(input("Your guess is warm\n"))
    elif(diff <= 8):
        num_guess = int(input("Your guess is cold\n"))
    elif(diff <= 13):
        num_guess = int(input("Your guess is very cold\n"))
    elif(diff <= 20):
        num_guess = int(input("Your guess is extremely cold\n"))
    else:
        num_guess = int(input("Your guess is icy freezing miserably cold\n"))
    
    return num_guess

def command(count):
    print("Congratulations. You figured it out in %d tries" %count)
    if(count == 1):
        print("That was lucky!")
    elif(2 <= count <= 4):
        print("That was amazing!")
    elif(5 <= count <= 6):
        print("That was okay.")
    elif(count == 7):
        print("Meh.")
    elif(8 <= count <= 9):
        print("This is not your game.")
    else:
        print("You are the worst guesser I've ever seen.")
            
def main():
    num_real = rnd.randint(1,50)
    print("Welcome to the Guessing Game!")
    num_guess = int(input("I picked a number between 1 and 50. Try and guess!\n"))
    print("You guessed",num_guess)
    diff = math.fabs(num_real - num_guess)
    count = 1
    while(diff != 0):
        num_guess = guess(diff)
        diff = math.fabs(num_real - num_guess)
        count += 1
    
    command(count)
    s = input("")
    if(s is not None):
        print("Game Over: You won!\n"
              "You guessed that the secret number was %d in %d tries."% (num_real,count))
    
main()