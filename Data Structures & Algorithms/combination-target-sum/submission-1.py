class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def rec(target,i,temp):
            if i==-1:
                # if target%nums[i] == 0:
                #     while target>0:
                #         temp.append(nums[0])
                #         target -= nums[0]
                if target == 0:
                    res.append(temp[:])
                return

            not_pick = rec(target,i-1,temp)
            if nums[i]<=target:
                temp.append(nums[i])
                pick = rec(target-nums[i],i,temp)
                temp.pop()
            return

        rec(target,n-1,[])
        return res