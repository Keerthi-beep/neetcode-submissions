class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.split(' ')
        s_new=''.join(s)
        print(s_new)
        x=''
        nums=[str(i) for i in range(10)]
        for i in s_new:
            if i.isalpha() or i in nums:
                x+=i
        x=x.lower()
        print(x)
        return x==x[::-1]