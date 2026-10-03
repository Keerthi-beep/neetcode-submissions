class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mp1 = [float('inf')]*26

        for i in range(len(words)):
            mp2 = [0]*26
            for ch in words[i]:
                mp2[ord(ch)-ord('a')] += 1
            for j in range(26):
                mp1[j] = min(mp1[j],mp2[j])

        res = []
        for i in range(26):
            for j in range(mp1[i]):
                res.append(chr(ord('a')+i))
        return res