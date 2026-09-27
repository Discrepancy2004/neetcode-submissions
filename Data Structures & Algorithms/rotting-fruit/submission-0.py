from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        path = set()
        q = deque()
        time = 0
        
        def rotten(r,c):
            if(r<0 or r>=rows or c>=cols or c<0 or grid[r][c] == 0 or grid[r][c] == 2):
                return
            path.add((r,c))
            q.append((r,c))
            grid[r][c] = 2

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while(q):
            for i in range(len(q)):
                r,c = q.popleft()
                
                rotten(r+1,c)
                rotten(r,c+1)
                rotten(r-1,c)
                rotten(r,c-1)
            if q:
                time = time + 1

            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return time


