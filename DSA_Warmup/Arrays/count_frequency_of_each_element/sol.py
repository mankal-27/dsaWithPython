from collections import Counter


class Solution:
    def count_frequency_nested_loop(self, nums):
        result = []
        for i in range(len(nums)):
            seen = False
            for j in range(i):
                if nums[i] == nums[j]:
                    seen = True
                    break
                if seen:
                    continue
                count = 0
                for k in range(i, len(nums)):
                    if nums[k] == nums[i]:
                        count += 1
                result.append([nums[i]], count)
        return result

    def count_frequency_hash_map(self, nums):
        counts = {}
        for v in nums:
            counts[v] = counts.get(v,0) + 1
        return [[v,c] for v, c in counts.items()]

    def count_frequency_builtin_counter(self, nums):
        return [[v,c] for v, c in Counter(nums).items()]
