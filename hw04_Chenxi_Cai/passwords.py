# Name: Chenxi Cai
# This program is to create unique user name and three suggested differnt passwords for user.
# Using the information: first name, last name and favorite word 
import random as rnd

# The unique user name and three different passwords will be computed below.
def main():
    print("Welcome to the username and password generator!")
    fname = input("Please enter your first name:")
    lname = input("Please enter your last name:")
    fa_word = input("Please enter your favorite word:")

    lname_long = lname + "******" # Add characters as necessary if the last name is shorter than seven characters.
    
    # User name = the first letter from first name, in lower case 
    # + the first seven letters from last name, in lower case 
    # + a random integer between 0 and 99
    usname = (fname[0] + lname_long[:7]).lower() + str(rnd.randint(0, 99))
    
    print("Thanks for your information. We create an unique user name for you:", usname)
    print("\nHere are three suggested passwords for you to consider:\n")
    
    # First password =  first + a random integer in the range 0 – 99 + last names
    # All characters are in lower case
    # Replacement: (a,@), (o,0), (l,1), (s,$), use table and translate function.
    fpass = fname.lower() + str(rnd.randint(0, 99)) + lname.lower() # First password before replacement
    table = str.maketrans("aols", "@01$") # Translate table
    fpass = fpass.translate(table)
    print("Password 1:", fpass)

    # Second password = firstname[first] in lower case + firstname[last] in upper case 
    # + lastname and favorite word with characters in same index and format.
    # list =  string[0].lower() + string[-1].upper() for string in [first name, last name, favorite word]
    # second password = "".join(list)
    info = [fname, lname, fa_word]
    spass ="".join([string[0].lower() + string[-1].upper() for string in info])
    print("Password 2:", spass)

    # Third password = combine random portions of three information 
    # Third password += string[0:random] in [first name, favorite word, last name]
    info_new = [fname, fa_word, lname]
    tpass = "" 
    for string in info_new:
        tpass += string[0:rnd.randint(0, len(string))]

    print("Password 3:", tpass)

main()