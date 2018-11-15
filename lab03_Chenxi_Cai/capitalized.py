#Write a short program that takes a string of input from the user 
# with any capitalization and prints out the string
# but with all consonants in lower case and all vowels in upper case.

def main(): 
    word = input("Please enter a string:\n")
    vowels = ['a','e','i','o','u']
    word_new = ""
    for i in word:
        if i.lower() in vowels:
            word_new += i.upper()
        else:
            word_new += i.lower()

    print("The new format is:\n" + word_new)

main()