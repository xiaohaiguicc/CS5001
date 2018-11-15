import sys

def main():
    height = int(sys.argv[1])
    #width = int(sys.argv[2])

    for h in range(height):
        print("*" * h)

    s = "abcd"
    print(s[0:1])
main()