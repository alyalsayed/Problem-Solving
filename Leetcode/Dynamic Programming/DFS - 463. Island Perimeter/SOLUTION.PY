class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        def dfs(row, col):
            nonlocal perimeter
            
            # Check if the current cell is out of bounds or a water cell
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                perimeter += 1
                return
            
            # Check if the current cell has been visited before
            if grid[row][col] == -1:
                return
            
            # Mark the current cell as visited
            grid[row][col] = -1
            
            # Explore the four neighbors
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        
        # Find the first land cell in the grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    return perimeter