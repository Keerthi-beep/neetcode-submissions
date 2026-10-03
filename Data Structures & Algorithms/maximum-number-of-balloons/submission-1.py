class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        req = 'balloon'
        mp = {}

        for ch in text:
            if ch in req:
                mp[ch] = mp.get(ch,0) + 1

        if len(mp)<5:
            return 0
            
        mp['l'] //= 2
        mp['o'] //= 2
        return min(mp.values())