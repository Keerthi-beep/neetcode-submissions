class Solution:
    def strStr(self, s: str, t: str) -> int:
        m,n = len(s),len(t)

        for i in range(m-n+1):
            j = 0
            while j<n:
                if s[i+j]!=t[j]:
                    break
                j += 1
            if j == n:
                return i
        return -1