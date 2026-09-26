class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid),len(grid[0])
        self.islands = 0
        path = set()
        def dfs(r,c):
            if c<0 or r<0 or c >= cols or r >= rows or (r,c) in path:
                return
            if grid[r][c] == '0':
                return
            
            path.add((r,c))

            dfs(r,c-1) 
            dfs(r-1,c)
            dfs(r +1 ,c)
            dfs(r,c+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in path:
                    self.islands += 1
                    dfs(i,j)
        
        return self.islands