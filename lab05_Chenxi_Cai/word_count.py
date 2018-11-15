# Prompts the user for a file name
# Prints out counts of words, non-whitespace characters 
# and alphanumeric characters

import re


def main():
    file_name = input("Enter the file name:\n")
    
    try:
        with open(file_name) as f:
         lines = f.read()
    except FileNotFoundError:
        print("Can't open", file_name)
    else:
        #counts of words 
        # p1 = re.compile(r'[\s\n]+')
        # whole_word = p1.split(lines)
        p1 = re.compile(r'\S+')
        whole_word = p1.findall(lines)
        count_word = len(whole_word)
        print("Words:", count_word)

        # non-whitespace characters
        p2 = re.compile(r'\S')
        whole_cha = p2.findall(lines)
        count_cha = len(whole_cha)
        print("Characters:", count_cha)
        
        # alphanumeric characters
        count_al = 0
        p3 = re.compile(r'\w')
        alpnum_whole = p3.findall(lines)
        count_al = len(alpnum_whole)
        print("Letters & numbers:", count_al)


main()