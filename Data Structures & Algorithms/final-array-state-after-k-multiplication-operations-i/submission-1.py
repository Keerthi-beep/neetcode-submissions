class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq,(nums[i],i))

        while k>0:
            minn,idx = heapq.heappop(pq)
            minn *= multiplier
            nums[idx] = minn
            heapq.heappush(pq,(minn,idx))
            k -=  1
        
        return nums