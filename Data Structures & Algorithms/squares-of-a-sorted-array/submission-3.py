class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        idx = -1
        n = len(nums)

        for i in range(1,n):
            if abs(nums[i])>abs(nums[i-1]):
                idx = i-1
                print(idx)
                break
        if idx == -1:
            idx = n-1
        res.append(nums[idx]**2)
        
        l,r = idx-1,idx+1

        while l>=0 and r<n:
            if abs(nums[l])<abs(nums[r]):
                res.append(nums[l]**2)
                l -= 1
            else:
                res.append(nums[r]**2)
                r += 1

        while l>=0:
            res.append(nums[l]**2)
            l -= 1

        while r<n:
            res.append(nums[r]**2)
            r += 1

        return res