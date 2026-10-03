class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix,suffix = [0]*n,[0]*n
        maxx = 0
        for i in range(n):
            if height[i]>maxx:
                maxx = height[i]
            prefix[i] = maxx
        
        maxx = 0
        for i in range(n-1,-1,-1):
            if height[i]>maxx:
                maxx = height[i]
            suffix[i] = maxx

        #print(prefix,suffix)

        res = 0
        for i in range(1,n-1):
            res += min(prefix[i],suffix[i])-height[i]
        return res