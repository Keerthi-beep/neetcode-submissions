class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st = {}
        for ch in s:
            st[ch] = st.get(ch,0)+1

        for ch in t:
            if ch not in st:
                return ch
            else:
                st[ch] -= 1
                if st[ch]==0:
                    st.pop(ch)

        return ''