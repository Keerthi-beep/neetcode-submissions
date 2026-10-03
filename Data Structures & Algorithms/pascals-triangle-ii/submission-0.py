class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        # if rowIndex == 0:
        #     return prev
        for row in range(1,rowIndex+1):
            temp = [1]
            for i in range(row-1):
                s = prev[i]
                if i<len(prev)-1:
                    s+=prev[i+1]
                temp.append(s)
            temp.append(1)
            prev = temp[:]
            print(prev)
        return prev