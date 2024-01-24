class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            j = target - nums[i]
            j_index = nums.index(target - nums[i]) if j in nums else -1
            if j in nums and i != j_index: return[i,j_index]