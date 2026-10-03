class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        a,b = 0,0

        for i in range(0,n,2):
            a += piles[i]
            b += piles[i+1]

        return True if a!=b else False