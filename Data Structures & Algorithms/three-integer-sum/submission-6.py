class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            t=-nums[i]
            while(l<r):
                print(i,l,r)
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif nums[l]+nums[r]>t:
                    r-=1
                elif nums[l]+nums[r]<t:
                    l+=1
        x=res
        # for i in res:
        #     if i not in x:
        #         x.append(i)
        return x