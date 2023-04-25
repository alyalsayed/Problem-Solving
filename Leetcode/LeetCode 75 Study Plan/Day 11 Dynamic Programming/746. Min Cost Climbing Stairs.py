class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Initialize the first two elements of a and b as the cost of the first and second step
        a, b = cost[0], cost[1]
        
        # Iterate over the remaining steps of the cost array
        for i in range(2, len(cost)):
            # Calculate the minimum cost of reaching the current step by taking the minimum of a and b,
            # adding the cost of the current step, and storing the result in ans
            ans = min(a, b) + cost[i]
            
            # Update the values of a and b to be the previous values of b and ans, respectively
            a, b = b, ans
        
        # Return the minimum of a and b, since we can reach the top of the floor by taking either the n-1 step or the n-2 step
        return min(a, b)

## or 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Get the length of the cost array
        n = len(cost)
        
        # Iterate over the cost array starting from the third element
        for i in range(2, n):
            # Update the cost of reaching the current step by adding the minimum cost of reaching the previous
            # two steps, and storing the result in the current element of the cost array
            cost[i] += min(cost[i-1], cost[i-2])
        
        # Return the minimum cost of reaching the last two steps of the floor
        return min(cost[n-1], cost[n-2])