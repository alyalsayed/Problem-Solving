class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_rows, num_cols = len(grid), len(grid[0])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        num_islands = 0
        
        # Define a helper function to perform DFS traversal
        def dfs(row, col):
            # Check if the current cell is within the grid and contains a '1'
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols or grid[row][col] == '0' or visited[row][col]:
                return
            
            # Mark the current cell as visited
            visited[row][col] = True
            
            # Recursively explore the adjacent cells
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        # Iterate over each cell in the grid
        for row in range(num_rows):
            for col in range(num_cols):
                # If the current cell is unvisited and contains a '1', start a new DFS traversal
                if not visited[row][col] and grid[row][col] == '1':
                    dfs(row, col)
                    num_islands += 1
        
        return num_islands