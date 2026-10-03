class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cnt = 0
        grid = [[0]*n for _ in range(n)]
        self.backtrack(grid,0,n)
        return self.cnt

    def backtrack(self,grid,i,n):
        if i==n:
            self.cnt += 1
            return True

        for j in range(n):
            if self.is_safe(grid,i,j,n):
                grid[i][j] = 1
                self.backtrack(grid,i+1,n)
                grid[i][j] = 0
        return False

    def is_safe(self,grid,row,col,n):
        for i in range(row):
            if grid[i][col] == 1:
                return False

        r,c = row-1, col-1
        while r>=0 and c>=0:
            if grid[r][c]==1:
                return False
            r-=1
            c-=1

        r,c = row-1, col+1
        while r>=0 and c<n:
            if grid[r][c]==1:
                return False
            r-=1
            c+=1
        
        return True
        