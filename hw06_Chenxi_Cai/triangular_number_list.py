"""
repeatedly prompts the user for numbers
(until the user inputs done)
and adds the corresponding triangular number to a list.
"""

def triangular_number(num):
    """corresponding triangular number"""
    tria_num = int(num * (num + 1) / 2)
    return tria_num


def main():
    string = input("Enter a number, or enter 'done': ")
    tria_list = []
    while string != "done":
        num = int(string)
        tria_num = triangular_number(num)
        tria_list.append(tria_num)
        print("The triangular number for {} is {}"
              .format(num, tria_num))
        string = input("Enter a number, or enter 'done': ")

    print(tria_list)

main()
