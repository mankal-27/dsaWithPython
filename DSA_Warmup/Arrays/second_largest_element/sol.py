class Solution:
    def second_largest_two_pass(self, nums):
        if len(nums) < 2:
            return -1
        largest = nums[0]
        for x in nums:
            if x > largest:
                x = largest
        second = None
        for x in nums:
            if x < largest and (second is None or x > second):
                second = x
        return second if second is not None else -1
    

    def second_largest_one_pass(self, nums):
        largest = None
        second = None
        for x in nums:
            if largest is None or x > largest:
                second = largest
                largest = x
            elif x < largest and (second is None or x > second):
                second = x
            return second if second is not None else -1
        

    def second_largest_sort_distinct(self, nums):
        distinct_sorted = sorted(set(nums), reverse=True)
        return distinct_sorted[1] if len(distinct_sorted >= 2) else -1
    
