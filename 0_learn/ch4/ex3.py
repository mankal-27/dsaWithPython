def merge_sort(a_list):  # sorts a_list in place using merge sort
    if len(a_list) > 1:  # base case: a list of 0 or 1 items is already sorted
        mid = len(a_list) // 2  # index of the middle element (integer division)
        left_half = a_list[:mid]  # copy of the first half
        righ_half = a_list[mid:]  # copy of the second half
        merge_sort(left_half)  # recursively sort the left half
        merge_sort(righ_half)  # recursively sort the right half

        left_ind = 0  # current position in left_half
        right_ind = 0  # current position in righ_half
        alist_ind = 0  # current position in the original list to write into

        # merge: runs while both halves still have unused elements
        while left_ind < len(left_half) and right_ind < len(righ_half):
            if left_half[left_ind] <= righ_half[right_ind]:  # left item is smaller or equal (<= keeps the sort stable)
                a_list[alist_ind] = left_half[left_ind]  # place the left item into the original list
                left_ind += 1  # move to the next left item
            else:  # right item is smaller
                a_list[alist_ind] = righ_half[right_ind]  # place the right item into the original list
                right_ind += 1  # move to the next right item
            alist_ind += 1  # advance the write position either way

        # copy any leftover items from the left half (right half ran out first)
        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]  # place the remaining left item
            left_ind += 1  # move to the next left item
            alist_ind += 1  # advance the write position

        # copy any leftover items from the right half (left half ran out first)
        while right_ind < len(righ_half):
            a_list[alist_ind] = righ_half[right_ind]  # place the remaining right item
            right_ind += 1  # move to the next right item
            alist_ind += 1  # advance the write position
