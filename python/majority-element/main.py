class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        max_count, max_val = 0, 0
        for i in set(nums):
            c = nums.count(i)
            if c > max_count: max_count, max_val = c, i
        return max_val