class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #freq ele and length of array
        mp = Counter(nums)
        listt = []
        for k,v in mp.items():
            listt.append((v,k))
        listt.sort(reverse=True)
        maxx_ele = listt[0][1]
        freq = listt[0][0]

        n = len(nums)
        cnt = 0
        for i in range(n):
            if nums[i] == maxx_ele:
                cnt += 1
            if cnt*2 > i+1 and (freq-cnt)*2 > (n-i-1):
                return i

        return -1