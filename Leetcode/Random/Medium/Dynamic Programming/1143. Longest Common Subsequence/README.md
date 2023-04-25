# Longest Common Subsequence

### link :

https://leetcode.com/problems/longest-common-subsequence/

Given two strings `text1` and `text2`, the `longestCommonSubsequence` method in the `Solution` class returns the length of the longest common subsequence of `text1` and `text2`. A subsequence is a sequence that can be derived from a string by deleting some or no elements without changing the order of the remaining elements, and is common to both strings if it appears in both strings in the same order.

## Example

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: One possible longest common subsequence is "ace".


## Solution: Dynamic Programming

The solution to the problem uses dynamic programming to solve the problem. We first initialize a 2D array `dp` of size `(n1+1) x (n2+1)` where `n1` and `n2` are the lengths of `text1` and `text2`, respectively. The value `dp[i][j]` represents the length of the longest common subsequence of the substrings `text1[:i]` and `text2[:j]`.

We then set the base cases where `i == 0` or `j == 0` to `dp[i][j] = 0` since either `text1` or `text2` is empty, and an empty string has no common subsequence with any other string.

We then fill up the rest of the array in a bottom-up manner using the following recurrence relation:

- If `text1[i-1] == text2[j-1]` (i.e., the current characters match), then the length of the longest common subsequence of `text1[:i]` and `text2[:j]` is `dp[i-1][j-1] + 1`, since we can include the current character in the common subsequence and the remaining substrings `text1[:i-1]` and `text2[:j-1]` also have a common subsequence.
- If `text1[i-1] != text2[j-1]` (i.e., the current characters do not match), then the length of the longest common subsequence of `text1[:i]` and `text2[:j]` is the maximum of `dp[i-1][j]` and `dp[i][j-1]`, since we can either exclude the current character from `text1` and continue with `text1[:i-1]` and `text2[:j]`, or exclude the current character from `text2` and continue with `text1[:i]` and `text2[:j-1]`.

The final answer is stored in `dp[n1][n2]`, where `n1` and `n2` are the lengths of `text1` and `text2`, respectively.

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n1][n2]
```

### Complexity Analysis
Time complexity: O(n1 x n2), where n1 and n2 are the lengths of the input strings text1 and text2, respectively. This is because we fill up a 2D array of size (n1+1) x (n2+1), where each entry takes constant time to compute using the recurrence relation.
Space complexity: O(n1 x n2), since we need to store the 2D array of size (n1+1) x (n2+1).

### Conclusion
We have solved the "Longest Common Subsequence" problem using dynamic programming. The time and space complexity of the solution are both O(n1 x n2), where n1 and n2 are the lengths of the input strings text1 and text2, respectively.