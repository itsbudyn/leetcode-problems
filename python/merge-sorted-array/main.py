class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(n): nums1.pop(-1)
        while nums2:
            moved = False
            for i in range(len(nums1)):
                if nums2[0] <= nums1[i]:
                    moved = True
                    nums1.insert(i,nums2[0])
                    break
            if not moved: nums1.append(nums2[0])
            nums2.pop(0)
        print(nums1)

nums1 = [1]
nums2 = []
m = 1
n = 0

x = Solution()
x.merge(nums1,m,nums2,n)