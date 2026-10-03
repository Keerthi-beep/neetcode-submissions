class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        mp = {}
        for num in nums:
            mp[num] = mp.get(num,0)+1

        freq = [[] for _ in range(n+1)]
        for key,val in mp.items():
            freq[val].append(key)

        res = []
        for i in range(n,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res