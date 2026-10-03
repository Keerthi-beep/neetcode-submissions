class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        req = 'balloon'
        mp = {}

        for ch in text:
            if ch in req:
                mp[ch] = mp.get(ch,0) + 1

        if len(mp)<5:
            return 0
        ans = float('inf')
        for k,v in mp.items():
            if k == 'l' or k=='o':
                ans = min(ans,v//2)
            else:
                ans = min(ans,v)
        return ans