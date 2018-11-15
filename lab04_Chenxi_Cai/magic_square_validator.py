

def main():
    print("Enter a magic number:")
    s = ""
    for i in range(3):
        s += input()
    
    for i in range(3):
        # horizontal rows
        if((int(s[3 * i]) + int(s[3 * i + 1]) + int(s[3 * i +2])) != 15):
            print("Not a magic square!")
            break
        # vertical columns
        if((int(s[i]) + int(s[i + 3]) + int(s[i + 6])) != 15):
            print("Not a magic square!")
            break
    else:
        #  corner-to-corner diagonals
        if((int(s[0]) + int(s[4]) + int(s[8])) != 15 
            or (int(s[2]) + int(s[4]) + int(s[6])) != 15):
            print("Not a magic square!")
        else:
            print("This is a magic square!")
        


main()