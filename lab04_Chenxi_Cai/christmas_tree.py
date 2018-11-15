# Draw a christmas tree with input of number of base

def main():
    width = int(input("Please enter an odd-valued of 3 or greater representing the width of the tree:\n"))
    if(width % 2 == 0):
        width = int(input("The value should be odd-valued. Please enter again:\n"))

    half = width // 2
    print(" " * half + "*")

    for i in range(0, half-1):
        print(" " * (half - i - 1) + "/" + " " * (2 * i + 1) + "\\")

    print("/" + "_" * (width - 2) + "\\")

main()