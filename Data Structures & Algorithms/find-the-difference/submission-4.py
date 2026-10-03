class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch,0)+1
        for ch in t:
            if ch not in mp:
                return ch
            mp[ch] -= 1
            if mp[ch]==0:
                mp.pop(ch)
        return ''
