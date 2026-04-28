class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        area = 0
        direction = [(-1,0),(0,-1),(0,1),(1,0)]
        rows,cols = len(grid), len(grid[0])

        def DFS(row,col):

            if (row<0 or col<0 or row>=rows or col>=cols or grid[row][col] == 0):
                return 0 

            grid[row][col] = 0
            area = 1
            for dr, dc in direction:
                area = area + DFS(dr+row, dc+col)

            return area

            

        for row in range(rows):
            for col in range (cols):
                if grid[row][col] == 1:
                    area = max (area,DFS(row,col))


                
        return area 
        