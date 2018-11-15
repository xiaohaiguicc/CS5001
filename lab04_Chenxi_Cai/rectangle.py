# Ask user which single character (e.g., &, #, +, n, s, 3) would like to use
# Ask the user for the rectangle’s width and height

def main():
    sym = input("Please enter a character (e.g., &, #, +, n, s, 3) as a symbol to make a rectangle:\n")
    height = int(input("Please enter the height of the rectangle:\n"))
    if(height < 2):
        print("The height value is too small to draw a rectangle.")
        height = int(input("Please enter the height of the rectangle:\n"))

    width = int(input("Please enter the width of the rectangle:\n"))
    if(width < 2):
        print("The width value is too small to draw a rectangle.")
        width = int(input("Please enter the width of the rectangle:\n"))

    print(sym * width)
    for i in range(height - 2):
        print(sym + " " * (width - 2) + sym)
    print(sym * width)

main()