#Judge if the input word is a palindrome
def main():
    choice = "y"
    while(choice == "y"):  
        word = input("Enter a potential palindrome:")
        length = len(word)
        for i in range(length//2):
            if(word[i] == word[length-i-1]):
                continue
            else:
                print("It is not a palindrome")
                break
        else:
            print("It is a palindrome")
        choice = input("Would you like to enter another palindrome?")

main()

