# 53. Maximum Subarray

### Link :

https://leetcode.com/problems/maximum-subarray/

Problem Statement
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2
Input: [1]
Output: 1

## Solution
This problem can be solved using dynamic programming. We can define a state dp[i] as the maximum sum of a subarray ending at index i. To calculate dp[i], we need to find the maximum sum of a subarray ending at index i-1 and add the current element nums[i]. If the sum of the subarray ending at index i-1 is negative, we can start a new subarray from index i.

Here is the Python code for the dynamic programming solution:

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        curr_sum = nums[0]
        
        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
```

In this solution, we keep track of the maximum sum seen so far (max_sum) and the current sum of the subarray ending at the current index (curr_sum). We iterate over the array from index 1 to n-1 and update curr_sum to be the maximum of the current element or the sum of the current element and the previous subarray sum. We then update max_sum to be the maximum of max_sum and curr_sum. Finally, we return max_sum as the maximum sum of the contiguous subarray.

This approach has a time complexity of O(n) and a space complexity of O(1), which is optimal for this problem.