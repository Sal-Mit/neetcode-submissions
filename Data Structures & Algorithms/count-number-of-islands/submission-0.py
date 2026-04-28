class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        #since we are using python for implementation 
        #and Python default recurrsion limit is ~1000
        #we will use BFS or iterative DFS
        #from collections import deque

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        land = 0

        def BFS(row, col):
            q=deque()
            grid[row][col] = "0"
            q.append((row,col))

            while q:
                rrow,ccol = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+rrow, dc+ccol
                    if (nr<0 or nc<0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    BFS(row,col)
                    land += 1

        return land




      

            

        