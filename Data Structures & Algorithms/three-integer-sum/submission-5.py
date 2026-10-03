class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        #-1,-1,0,1,2,4
        #-2,0,1,1,2
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            t=-nums[i]
            while(l<r):
                print(i,l,r)
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[l]+nums[r]>t:
                    r-=1
                elif nums[l]+nums[r] < t:
                    l+=1
        x=[]
        for i in res:
            if i not in x:
                x.append(i)
        return x