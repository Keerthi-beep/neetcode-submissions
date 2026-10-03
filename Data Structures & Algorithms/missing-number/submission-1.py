class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        actual = (n*(n+1))//2
        summ = sum(nums)
        diff = actual-summ
        if diff != 0:
            return diff
        if 0 in nums:
            return n+1
        else:
            return 0
        