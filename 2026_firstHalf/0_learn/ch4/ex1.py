def bubble_sort(a_list):
    # Last valid index; also the number of adjacent pairs to compare in the first pass
    list_length = len(a_list) - 1

    # Each outer pass "bubbles" the largest unsorted element to the end
    for i in range(list_length):
        swapped = False
        # After i passes, the last i elements are already in place, so skip them
        for j in range(list_length - i):
            # Out of order: left neighbour is bigger than the right one
            if a_list[j] > a_list[j + 1]:
                # Swap the pair in place (tuple swap, no temp variable needed)
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                swapped = True
        # No swaps in a full pass means the list is sorted: stop early (best case O(n))
        if not swapped:
            break
    # The list is sorted in place; returned for convenience
    return a_list
