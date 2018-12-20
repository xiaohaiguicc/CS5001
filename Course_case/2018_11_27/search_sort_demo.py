from search import Search
from sort import Sort
import sys


def main(search_or_sort):
    """Run demo searches"""
    if search_or_sort == "search":
        demo_search([50, 20, 14, 5, 2, -10, -25, -30], -25, "linear")
        demo_search([50, 20, 14, 5, 2, -10, -25, -30], 100, "linear")
        demo_search([-50, -20, 0, 5, 14, 69, 120, 121], 120, "binary")
        demo_search([-50, -20, 0, 5, 14, 69, 120, 121], 100, "binary")

    """Run demo sorts"""
    if search_or_sort == "sort":
        print("Sorting a totally un-ordered list:")
        demo_sort([50, 20, 14, 5, 2, -10, -25, -30], "selection")
        demo_sort([50, 20, 14, 5, 2, -10, -25, -30], "bubble")

        print("Sorting a partially-ordered list:")
        demo_sort([1, -28, 67, 3, 25, -82, 21, 81], "selection")
        demo_sort([1, -28, 67, 3, 25, -82, 21, 81], "bubble")

        print("Sorting an already-ordered list:")
        demo_sort([-50, -20, 0, 5, 14, 69, 120, 121], "selection")
        demo_sort([-50, -20, 0, 5, 14, 69, 120, 121], "bubble")


def demo_search(array, value, search):
    print("=======", search, "search")
    print(array)
    print("Searching for", value)
    if (search == "linear"):
        found = Search.linear_search(array, value)
    else:
        found = Search.binary_search(array, value)

    if found >= 0:
        print("Found", value, "at index:", found)
    else:
        print("Failed to find", value)

    print("\n")


def demo_sort(array, sort):
    print("=======", sort, "sort")
    print("Before sorting:")
    print(array)
    if (sort == "selection"):
        Sort.selection_sort(array)
    else:
        Sort.bubble_sort(array)
    print("After sorting:")
    print(array)

    print("\n")

main(sys.argv[1])