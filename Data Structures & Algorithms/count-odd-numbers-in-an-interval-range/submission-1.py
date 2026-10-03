class Solution:
    def countOdds(self, low: int, high: int) -> int:
        cnt = (high-low+1)//2
        if low%2!=0 and high%2!=0:
            cnt += 1
        return cnt
        