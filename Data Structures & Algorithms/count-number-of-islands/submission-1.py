class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        path = set()
        self.islands = 0

        def dfs(r,c):
            if (r,c) in path or r < 0 or r>=len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == "0":
                return 
            
            path.add((r,c))

            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r+1,c)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i,j) not in path:
                    dfs(i,j)
                    self.islands += 1

        return self.islands
