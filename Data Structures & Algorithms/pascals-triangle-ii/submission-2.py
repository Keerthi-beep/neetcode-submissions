class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]

        for row in range(1,rowIndex+1):
            temp = [1]
            for i in range(row-1):
                temp.append(prev[i]+prev[i+1])
            temp.append(1)
            prev = temp[:]
            
        return prev