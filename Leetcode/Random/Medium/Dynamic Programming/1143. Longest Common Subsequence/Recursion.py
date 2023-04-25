class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.lcs(text1, text2, len(text1), len(text2), memo)

    def lcs(self, text1: str, text2: str, m: int, n: int, memo: dict) -> int:
        if m == 0 or n == 0:
            return 0
        if (m, n) in memo:
            return memo[(m, n)]
        if text1[m-1] == text2[n-1]:
            memo[(m, n)] = 1 + self.lcs(text1, text2, m-1, n-1, memo)
            return memo[(m, n)]
        else:
            memo[(m, n)] = max(self.lcs(text1, text2, m-1, n, memo), self.lcs(text1, text2, m, n-1, memo))
            return memo[(m, n)]