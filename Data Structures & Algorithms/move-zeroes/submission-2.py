class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        while i<n:
            start = i
            while start<n-1 and nums[start]==0:
                start += 1
            nums[i],nums[start] = nums[start],nums[i]
            i += 1