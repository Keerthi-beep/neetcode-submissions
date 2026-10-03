class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 1
        s = ''
        i = 1
        n = len(chars)

        while i<n:
            cnt = 1
            while i< n and chars[i]==chars[i-1]:
                cnt += 1
                i += 1
            s += chars[i-1]
            if cnt>1:
                s += str(cnt)
            i += 1

        if cnt == 1 or (n>1 and chars[n-1]!=chars[n-2]):
            s += chars[n-1]
        

        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)
        