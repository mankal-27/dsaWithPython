from bisect import bisect_right  # binary search helper: finds insertion index in a sorted list


def insertion_sort_basic(a_list):
    # Original version: sorts a_list in place (and returns it) using a linear scan
    for i in range(1, len(a_list)):  # a_list[:i] is always sorted; start at 1 since one element is trivially sorted
        value = a_list[i]  # element to insert into the sorted prefix

        while i > 0 and a_list[i - 1] > value:  # walk left while the previous element is larger than value
            a_list[i] = a_list[i - 1]  # shift the larger element one slot to the right
            i = i - 1  # move the scan position one step left
        a_list[i] = value  # drop the value into the gap that was opened
    return a_list  # return the same list for convenience


def insertion_sort(a_list):
    # Optimized version: sorts a_list in place (and returns it) using binary insertion sort
    for i in range(1, len(a_list)):  # a_list[:i] is always sorted; start at 1 since one element is trivially sorted
        value = a_list[i]  # element to insert into the sorted prefix

        if a_list[i - 1] <= value:  # already in place (common on nearly-sorted input), skip the work
            continue

        pos = bisect_right(a_list, value, 0, i)  # binary search: O(log i) comparisons; bisect_right keeps the sort stable
        a_list[pos + 1:i + 1] = a_list[pos:i]  # shift the larger elements right by one in a single C-level slice move
        a_list[pos] = value  # drop the value into its sorted position
    return a_list  # return the same list for convenience
