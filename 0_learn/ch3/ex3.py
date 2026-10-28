from bisect import bisect_left

sorted_fruits = ['apple', 'bananna','kiwi', 'orange']
print(bisect_left(sorted_fruits, 'kiwi'))

def binary_search(an_iterable, target):
    index = bisect_left(an_iterable, target)

    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False

 