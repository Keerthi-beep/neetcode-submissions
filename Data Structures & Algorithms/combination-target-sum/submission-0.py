class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def backtrack(idx,ds,ans):
            if idx==len(nums):
                return
            ds.append(nums[idx])
            if sum(ds)==target:
                ans.append(ds[:])
            
            if sum(ds)<target:
                backtrack(idx,ds,ans)
            ds.pop()
            backtrack(idx+1,ds,ans)

        ans=[]
        ds=[]
        backtrack(0,ds,ans)
        return ans