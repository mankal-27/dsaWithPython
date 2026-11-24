class Solution:
    # ---------- Brute force: slicing creates new lists at every level ----------
    def mergeSortBruteForce(self, nums):
        if len(nums) <= 1:
            return nums[:]
        mid = len(nums) // 2
        left_sorted = self.mergeSortBruteForce(nums[:mid])   # O(n) copy
        right_sorted = self.mergeSortBruteForce(nums[mid:])  # O(n) copy
        return self.mergeTwoSorted(left_sorted, right_sorted)

    def mergeTwoSorted(self, left_list, right_list):
        merged = []
        left = right = 0
        while left < len(left_list) and right < len(right_list):
            if left_list[left] <= right_list[right]:  # <= keeps it stable
                merged.append(left_list[left])
                left += 1
            else:
                merged.append(right_list[right])
                right += 1
        merged.extend(left_list[left:])
        merged.extend(right_list[right:])
        return merged

    # ---------- Optimized: in-place on index ranges, no slicing ----------
    def mergeSortOptimized(self, nums):
        self.sortRange(nums, 0, len(nums) - 1)
        return nums

    def sortRange(self, nums, low, high):
        if low >= high:  # base case: 0 or 1 element
            return
        mid = (low + high) // 2
        self.sortRange(nums, low, mid)
        self.sortRange(nums, mid + 1, high)
        self.mergeRange(nums, low, mid, high)

    def mergeRange(self, nums, low, mid, high):
        temp = []
        left, right = low, mid + 1
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
        # copy back (the step missing in my_sol.py)
        for offset in range(len(temp)):
            nums[low + offset] = temp[offset]
