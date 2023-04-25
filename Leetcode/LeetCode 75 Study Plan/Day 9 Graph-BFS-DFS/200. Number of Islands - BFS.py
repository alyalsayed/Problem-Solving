class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_rows, num_cols = len(grid), len(grid[0])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        num_islands = 0
        
        # Define a helper function to perform BFS traversal
        def bfs(row, col):
            queue = [(row, col)]
            
            while queue:
                curr_row, curr_col = queue.pop(0)
                
                # Check if the current cell is within the grid and contains a '1'
                if curr_row < 0 or curr_row >= num_rows or curr_col < 0 or curr_col >= num_cols or grid[curr_row][curr_col] == '0' or visited[curr_row][curr_col]:
                    continue
                
                # Mark the current cell as visited
                visited[curr_row][curr_col] = True
                
                # Add the adjacent cells to the queue
                queue.append((curr_row+1, curr_col))
                queue.append((curr_row-1, curr_col))
                queue.append((curr_row, curr_col+1))
                queue.append((curr_row, curr_col-1))
        
        # Iterate over each cell in the grid
        for row in range(num_rows):
            for col in range(num_cols):
                # If the current cell is unvisited and contains a '1', start a new BFS traversal
                if not visited[row][col] and grid[row][col] == '1':
                    bfs(row, col)
                    num_islands += 1
        
        return num_islands