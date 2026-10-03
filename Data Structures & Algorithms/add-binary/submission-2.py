class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)

        i,j = m-1,n-1
        res = ''
        carry = 0

        while i>=0 and j>=0:
            s = int(a[i]) + int(b[j]) + carry
            res += str(s%2)
            print(res)
            carry = s//2
            i -= 1
            j -= 1

        while i>=0:
            s = int(a[i]) + carry
            res += str(s%2)
            carry = s//2
            i -= 1
        while j>=0:
            s = int(b[j]) + carry
            res += str(s%2)
            carry = s//2
            j -= 1
        if carry:
            res+=str(carry)
        return res[::-1]