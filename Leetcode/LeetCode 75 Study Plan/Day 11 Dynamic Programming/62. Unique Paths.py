class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D DP array of size m x n
        dp = [[1 for j in range(n)] for i in range(m)]
        
        # Fill the DP array iteratively
        for i in range(1, m):
            for j in range(1, n):
                # Use the formula dp[i][j] = dp[i-1][j] + dp[i][j-1]
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return the bottom-right corner of the DP array, which represents the total number of unique paths
        return dp[m-1][n-1]