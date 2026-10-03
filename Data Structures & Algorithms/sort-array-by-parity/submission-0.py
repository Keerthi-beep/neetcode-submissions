class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i]%2 !=0:
                j = i+1
                while j<n and nums[j]%2!=0:
                    j += 1
                if j<n:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums