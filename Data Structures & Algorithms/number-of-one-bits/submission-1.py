class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            ones = n&1
            cnt += ones
            n = n>>1
        return cnt