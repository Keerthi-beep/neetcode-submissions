class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash={
            '}':'{',
            ']':'[',
            ')':'('
        }

        for i in s:
            if i in hash:
                if not stack or stack[-1]!=hash[i]:
                    return False
                stack.pop()
            if i in hash.values():
                stack.append(i)
        return len(stack)==0
