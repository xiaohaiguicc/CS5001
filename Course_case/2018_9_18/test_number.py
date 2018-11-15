import random as rnd

def main():
    number_real = rnd.randint(1,10)
    number_guess = int(input("Please input an interger between 1 and 10: "))
    counter = 1

    while(number_guess != number_real):
        if(number_guess > number_real):
            number_guess = int(input("Please input a sammer number:"))
        else:
            number_guess = int(input("Please input a larger number:"))
        counter += 1 

    print("Congratulation! You get the right number! The times you guess is:",counter )


main()