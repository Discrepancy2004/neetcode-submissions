class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        path = set()
        self.area = 0
        self.maxArea = 0
        def dfs(r,c):
            if r<0 or r>= rows or c<0 or c>= cols or (r,c) in path:
                return

            if grid[r][c] == 0:
                return

            path.add((r,c))
            self.area = self.area + 1
            self.maxArea = max(self.maxArea,self.area)

            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)

        for i in range(rows):
            
            for j in range(cols):
                self.area = 0
                if grid[i][j] == 1 and (i,j) not in path:
                    dfs(i,j)

        return self.maxArea

