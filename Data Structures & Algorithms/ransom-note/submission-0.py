class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = [0]*256
        for ch in magazine:
            mp[ord(ch)-ord('a')] += 1

        for ch in ransomNote:
            if mp[ord(ch)-ord('a')] <= 0:
                return False
            mp[ord(ch)-ord('a')] -= 1
        
        return True