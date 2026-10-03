class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        nums = '1234567890'
        n = ''
        for ch in s:
            if ch==']':
                prev = ''
                while stack[-1]!='[':
                    a = stack.pop()
                    prev = a + prev
                stack.pop()
                num = int(stack.pop())
                stack.append(num*prev)
            elif ch in nums:
                n += ch
            else:
                if n!='':
                    stack.append(int(n))
                    n = ''
                stack.append(ch)
            
        return ''.join(x for x in stack) if stack else ''