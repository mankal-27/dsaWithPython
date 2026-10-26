def quick_sort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            # Choose pivot (last element)
            pivot = arr[high]
            i = low - 1

            # Partition
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            # Place pivot in correct position
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            pivot_idx = i + 1

            # Push sub-arrays to stack
            stack.append((pivot_idx + 1, high))
            stack.append((low, pivot_idx - 1))

    return arr