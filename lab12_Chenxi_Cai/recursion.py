import sys


def main():
    num_str = sys.argv[1]
    val = int(sys.argv[2])
    num_list1 = [int(num) for num in num_str]
    num_list2 = [int(num) for num in num_str]
    num_list3 = [int(num) for num in num_str]

    print("The list is:", num_list1, "value is: ", val)
    # sum
    print("sum_tail: ", add_list_tail(num_list1, 0, 0))
    print("sum_head: ", add_list_head(num_list1))
    # reverse
    print("reverse_tail: ",
          rev_list_tail(num_list2, len(num_list2) - 1, []))
    print("reverse_head: ", rev_list_head(num_list2))
    # linear
    print("linear search of ", val, "is: ",
          linear_search(val, num_list3, 0))
    # bubble sort
    print("bubble sort is: ",
          bubble_sort(num_list3, 0))
    # binary search
    print("binary search of ", val, "in", num_list3, "is: ",
          binary_search(val, num_list3, 0, len(num_list3) - 1))


# head
def add_list_head(num_list):
    """
    a recursive function that takes a list of numbers
    and returns the sum of the numbers
    """
    if num_list == []:
        return 0
    num = num_list.pop()
    return num + add_list_head(num_list)


# tail:
def add_list_tail(num_list, index, total):
    """
    a recursive function that takes a list of numbers
    and returns the sum of the numbers
    """
    if index == len(num_list):
        return total
    total += num_list[index]
    index += 1
    return add_list_tail(num_list, index, total)


# head
def rev_list_head(num_list):
    """
    a recursive function that takes a list
    and returns a list with the elements reversed
    """
    if num_list == []:
        return []
    num = num_list.pop()
    return [num] + rev_list_head(num_list)


# tail
def rev_list_tail(num_list, index, num_rev):
    """
    a recursive function that takes a list
    and returns a list with the elements reversed
    """
    if index == -1:
        return num_rev

    num_rev += [num_list[index]]
    index -= 1
    return rev_list_tail(num_list, index, num_rev)


#  tail
def linear_search(value, num_list, index):
    """
    a recursive function that takes a value and a list
    and returns the index of the value if the value is found in the list,
    and returns -1 if not, using the linear search algorithm.
    """
    if index == len(num_list):
        return -1
    if value == num_list[index]:
        return index
    return linear_search(value, num_list, index + 1)


def binary_search(value, num_list, start, end):
    """
    a recursive function that takes a value and a list
    and returns the index of the value if the value is found in the list,
    and returns -1 if not, using the binary search algorithm.
    """
    if start + 1 == end:
        if value == num_list[start]:
            return start
        elif value == num_list[end]:
            return end
        else:
            return -1
    elif start + 1 < end:
        mid = start + (end - start) // 2
        if num_list[mid] == value:
            return mid
        if value > num_list[mid]:
            start = mid
        else:
            end = mid
    return binary_search(value, num_list, start, end)


def bubble_sort(num_list, index):
    """
    a recursive function that takes a list
    and returns a list of the same elements, sorted.
    """
    if index == len(num_list):
        return num_list
    end = len(num_list) - index - 1
    num_list = helper(num_list, 0, end)
    index += 1
    return bubble_sort(num_list, index)


def helper(num_list, start, end):
    """
    a recursive function that takes a list, start and end index
    and returns a list of the same elements,
    list[end] is the biggest element in list[start : end + 1].
    """
    if start == end:
        return num_list
    if num_list[start] > num_list[start + 1]:
        num_list[start], num_list[start + 1] = (num_list[start + 1],
                                                num_list[start])

    start += 1
    return helper(num_list, start, end)

main()
