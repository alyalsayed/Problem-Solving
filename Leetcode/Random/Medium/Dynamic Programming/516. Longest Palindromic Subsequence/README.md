# Longest Palindromic Subsequence

### Link :

https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


## Solution 1: Dynamic Programming

The first solution to the problem uses dynamic programming to solve the problem. We first initialize a 2D array `dp` of size `n x n` where `n` is the length of the input string `s`. The value `dp[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i:j+1]`.

We then set the base cases where `i == j` to `dp[i][j] = 1` since a single character is always a palindrome. We then fill up the rest of the array in a bottom-up manner using the following recurrence relation:

- If `s[i] == s[j]`, then the length of the longest palindromic subsequence in `s[i:j+1]` is `dp[i+1][j-1] + 2`, since we can include both `s[i]` and `s[j]` in the subsequence and the remaining substring `s[i+1:j]` is also a palindrome.
- If `s[i] != s[j]`, then the length of the longest palindromic subsequence in `s[i:j+1]` is the maximum of `dp[i+1][j]` and `dp[i][j-1]`, since we can skip either `s[i]` or `s[j]` and continue with the remaining substring.

The final answer is stored in `dp[0][n-1]`.

```python

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]

```
### Complexity Analysis
Time complexity: O(n^2), where n is the length of the input string s. This is because we fill up a 2D array of size n x n, where each entry takes constant time to compute using the recurrence relation.
Space complexity: O(n^2), since we need to store the 2D array of size n x n.


## Solution 2: Recursion with Memoization

The second solution to the problem uses recursion with memoization to solve the problem. The longestPalindromeSubseq method calls the helper method, which takes in the input string s, indices i and j that represent the current substring we are considering, and a memo dictionary to store the results of the subproblems we have already solved.

The base cases are the same as the previous solution: if i > j, there are no characters in the substring, so the length of the palindromic subsequence is 0; if i == j, there is only one character in the substring, so the length of the palindromic subsequence is 1.

If the current first and last characters are the same, we can include them in the palindromic subsequence, so we add 2 to the length and recursively call the helper method on the remaining substring s[i+1:j-1].

If the current first and last characters are not the same, we have two options: we can either exclude the first character and recursively call the helper method on the substring s[i+1:j], or we can exclude the last character and recursively call the helper method on the substring s[i:j-1]. We take the maximum of these two options as the length of the palindromic subsequence.

To avoid redundant computations, we use memoization to store the results of the subproblems we have already solved. We store the length of the palindromic subsequence for the current substring s[i:j] in the memo dictionary using a tuple (i, j) as the key.

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        return self.helper(s, 0, len(s) - 1, memo)
    
    def helper(self, s, i, j, memo):
        if i > j:
            return 0
        if i == j:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        if s[i] == s[j]:
            memo[(i, j)] = 2 + self.helper(s, i + 1, j - 1, memo)
        else:
            memo[(i, j)] = max(self.helper(s, i + 1, j, memo), self.helper(s, i, j - 1, memo))
        return memo[(i, j)]

```
### Complexity Analysis
Time complexity: O(n^2), where n is the length of the input string s. This is because we need to solve O(n^2) subproblems, and each subproblem takes constant time to solve after memoization.
Space complexity: O(n^2), since we need to store the memo dictionary of size n x n to avoid redundant computations.
Conclusion
We have solved the "Longest Palindromic Subsequence" problem using two different approaches: dynamic programming and recursion with memoization. Both solutions have the same time and space complexity, but the recursive approach may be slower for larger input sizes due to the overhead of function calls and memoization.