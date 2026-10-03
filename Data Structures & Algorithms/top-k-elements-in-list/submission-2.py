class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for n in nums:
            mp[n] = mp.get(n,0)+1

        res = []
        for key,val in mp.items():
            res.append((val,key))

        # res.sort(reverse=True)
        # ans = []
        # for i in range(k):
        #     ans.append(res[i][1])
        # return ans

        pq = []
        for i in range(len(res)):
            heapq.heappush(pq,(res[i]))
            if i>=k:
                heapq.heappop(pq)

        return [x[1] for x in pq]