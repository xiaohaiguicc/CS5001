"""
prompts the user for two integers of any length
adds them together.
counts the number of times the "carry" operation
"""

def reverse_digit(num):
    """
    break a multi-digit integer
    into a list of digits
    reversed

    Keyword Argument:
    num -- string of integer
    """
    num_list = [int(n) for n in reversed(num)]
    return num_list

def add(num1, num2):
    """
    Add two integers

    Keyword Arguments:
    num1, num2 -- string of two integers
    """
    if len(num1) >= len(num2):
        short_list = reverse_digit(num2)
        long_list = reverse_digit(num1)
    else:
        short_list = reverse_digit(num1)
        long_list = reverse_digit(num2)

    sum_list = []
    carry_list = [0]
    for i in range(len(short_list)):
        sum = short_list[i] + long_list[i] + carry_list[i]
        sum_list.append(sum % 10)
        carry_list.append(sum // 10)

    for i in range(len(short_list), len(long_list)):
        sum = long_list[i] + carry_list[i]
        sum_list.append(sum % 10)
        carry_list.append(sum // 10)

    if carry_list[-1] == 1:
        sum_list.append(1)

    return sum_list, carry_list

def carry_count(carry_list):
    """
    count carry times

    Keyword Argument：
    carry_list: a list of carry or not
    """
    count = 0
    for i in carry_list:
        count += i
    return count

def main():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    sum_list, carry_list = add(num1, num2)
    count = carry_count(carry_list)
    print(num1 + " + " + num2 + " =", int(num1) + int(num2))
    print(sum_list)
    print("Number of carries:", count)


main()
