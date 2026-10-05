class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []

        def solve(i,temp):
            if i==len(digits):
                res.append(temp)
                return
            
            for ch in mp[int(digits[i])]:
                solve(i+1,temp+ch)

        solve(0,'')
        return res if res!=[''] else []