class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
            nums.append("_")
        return len(nums) - nums.count("_")