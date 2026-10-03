class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, n-1
        MOD = 1000000007
        res = 0

        while left<=right:
            while left <= right and nums[left]+nums[right]>target:
                right -= 1
            if left <= right:
                res += pow(2,right-left)
                res %= MOD
                left += 1

        return int(res)