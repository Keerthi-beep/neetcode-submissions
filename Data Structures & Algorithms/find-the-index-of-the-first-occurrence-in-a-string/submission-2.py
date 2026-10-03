class Solution:
    def strStr(self, s: str, t: str) -> int:
        i,j = 0,0
        m,n = len(s),len(t)
        start = -1

        while i<m and j<n:
            start = i
            while i<m and j<n and s[i] == t[j]:
                j += 1
                i += 1
            if j == n:
                return start
            else:
                j = 0
                i = start + 1

        return -1