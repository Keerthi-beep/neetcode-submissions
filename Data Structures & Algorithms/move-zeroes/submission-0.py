class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            if nums[i] == 0:
                cnt += 1

        k = 0
        for i in range(n):
            if nums[i]!=0 and (n-k)>0:
                nums[k]=nums[i]
                k += 1
            if i>=n-cnt:
                nums[i]=0
        