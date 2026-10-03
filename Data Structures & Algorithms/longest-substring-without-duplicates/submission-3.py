class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l,r=0,0
        hash={}
        while r<len(s):
            print(l,r)
            if s[r] in hash:
                if hash[s[r]]>=l:
                    l=hash[s[r]]+1
            res=max(res,r-l+1)
            hash[s[r]]=r
            r+=1
        return res