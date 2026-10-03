class Solution:
    def strStr(self, s: str, t: str) -> int:
        if t == '': return 0
        lps = [0]*len(t)
        prevlps, i = 0, 1

        while i<len(t):
            if t[i] == t[prevlps]:
                lps[i] = prevlps + 1
                prevlps += 1
                i += 1
            elif prevlps == 0:
                lps[i] = 0
                i += 1
            else:
                prevlps = lps[prevlps-1]

        i,j = 0,0
        while i<len(s):
            if s[i]==t[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == len(t):
                return i-len(t)

        return -1