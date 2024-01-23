class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ### nums = list(set(nums)) <- THIS SHOULD HAVE BEEN ACCEPTED !!!!!
        for i in set(nums):
            while nums.count(i) > 1: nums.remove(i)
        return len(nums)
    
x = Solution()

print(x.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))