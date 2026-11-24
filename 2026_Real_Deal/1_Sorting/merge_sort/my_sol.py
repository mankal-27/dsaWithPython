class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high+1):
            arr[i] = temp[i-low]

        # BUG: mergeSortHelper is indented inside merge(), so it is a nested function
        # that never runs and Solution has no such method. Dedent to class level.
        def mergeSortHelper(self, arr, low, high):
            if low >= high:
                return

            mid = (low + high) // 2
            self.mergeSortHelper(arr, low, mid)
            self.mergeSortHelper(arr, mid+1, high)
            self.merge(arr, low, mid, high)

        # BUG: same problem - nested inside merge(), so Solution().mergeSort() fails.
        def mergeSort(self, nums):
            n = len(nums)
            self.mergeSortHelper(nums, 0 , n - 1)
            return nums

        