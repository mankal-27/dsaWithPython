class Solution:
    def reverseArray(self, arr):  
        temp = [None] * len(arr)
        n = len(arr)
        for i in range(n-1, -1, -1):  
            temp[n-i-1] = arr[i] 

        for i in range(n):
            arr[i] = temp [i]

        return

    def reverseArrayOptimized(self, arr):
        left = 0
        right = len(arr) - 1
        while(left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

# Review: no bugs. Correct in-place reversal, but brute force (O(n) extra space).
# Optimized: two pointers swapping arr[left], arr[right] gives O(1) space.
