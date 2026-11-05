"""
Given a list of words in alphabetical order, write a function that performs a binary search for
a word and returns whether it is in the list.
"""

def findAletter(a_list, target):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid = (first + last) // 2

        if a_list[mid] == target:
            return True
        elif target < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


def findLetter(letters, target):
    """Binary search a sorted list of single letters, comparing by ord()."""
    first = 0
    last = len(letters) - 1
    target_code = ord(target)

    while first <= last:
        mid = (first + last) // 2
        mid_code = ord(letters[mid])

        if mid_code == target_code:
            return True
        elif target_code < mid_code:
            last = mid - 1
        else:
            first = mid + 1
    return False
